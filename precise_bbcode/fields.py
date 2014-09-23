# -*- coding: utf-8 -*-

# Standard library imports
from __future__ import unicode_literals
import re

# Third party imports
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import signals
from django.utils.translation import ugettext_lazy as _

# Local application / specific library imports
from .parser import get_parser


_rendered_content_field_name = lambda name: '_{}_rendered'.format(name)

_smiley_code_re = re.compile(r'^[\w|\S]+$')
validate_smiley_code = RegexValidator(_smiley_code_re, _("Enter a valid 'smiley code' consisting of any character without whitespace characters"), 'invalid')


class BBCodeContent(object):
    def __init__(self, raw, rendered=None):
        self.raw = raw
        self.rendered = rendered


class BBCodeTextCreator(object):
    """
    Acts as the Django's default attribute descriptor class (enabled via the SubfieldBase metaclass).
    The main difference is that it does not call to_python() on the BBCodeTextField class. Instead, it
    stores the two different values of a BBCode content (the raw and the rendered data) separately.
    These values can be separately updated when something is assigned. When the field is accessed,
    a BBCodeContent instance will be returned ; this one is built with the current data.
    """
    def __init__(self, field):
        self.field = field
        self.rendered_field_name = _rendered_content_field_name(self.field.name)

    def __get__(self, instance, type=None):
        if instance is None:
            return self.field
        raw_content = instance.__dict__[self.field.name]
        if raw_content is None:
            return None
        else:
            return BBCodeContent(raw_content, rendered=getattr(instance, self.rendered_field_name))

    def __set__(self, instance, value):
        if isinstance(value, BBCodeContent):
            instance.__dict__[self.field.name] = value.raw
            setattr(instance, self.rendered_field_name, value.rendered)
        else:
            # Set only the bbcode content field
            instance.__dict__[self.field.name] = self.field.to_python(value)


class BBCodeTextField(models.TextField):
    """
    A BBCode text field contributes two columns to the model instead of the standard single column.
    The initial column stores the BBCode content and the other one keeps the rendered content returned
    by the BBCode parser.
    """
    def __init__(self, *args, **kwargs):
        # For South FakeORM compatibility: the frozen version of a BBCodeTextField can't try to add a
        # '*_rendered' field, because the '*_rendered' field itself is frozen as well.
        self.add_rendered_field = not kwargs.pop('no_rendered_field', False)
        super(BBCodeTextField, self).__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name):
        self.raw_name = name

        if self.add_rendered_field and not cls._meta.abstract:
            self.rendered_field_name = _rendered_content_field_name(name)

            # Create a hidden 'rendered' field
            rendered = models.TextField(editable=False, null=True, blank=True)
            # Ensure that the 'rendered' field appears before the actual field in
            # the models _meta.fields
            rendered.creation_counter = self.creation_counter
            cls.add_to_class(self.rendered_field_name, rendered)

        # The data will be processed before each save
        signals.pre_save.connect(self.process_bbcodes, sender=cls)

        # Add the default text field
        super(BBCodeTextField, self).contribute_to_class(cls, name)

        # Associates the name of this field to a special descriptor that will return
        # an appropriate BBCodeContent object each time the field is accessed
        self.set_descriptor_class(cls)

    def set_descriptor_class(self, cls):
        setattr(cls, self.name, BBCodeTextCreator(self))

    def get_db_prep_save(self, value, connection):
        if isinstance(value, BBCodeContent):
            value = value.raw
        return super(BBCodeTextField, self).get_db_prep_save(value, connection)

    def process_bbcodes(self, signal, sender, instance=None, **kwargs):
        bbcode_text = getattr(instance, self.raw_name)

        if isinstance(bbcode_text, BBCodeContent):
            bbcode_text = bbcode_text.raw

        rendered = ''
        if bbcode_text:
            parser = get_parser()
            rendered = parser.render(bbcode_text)

        setattr(instance, self.rendered_field_name, rendered)


class SmileyCodeField(models.CharField):
    default_validators = [validate_smiley_code]
    description = _("Smiley code (up to %(max_length)s)")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 50)
        # Set db_index=True unless it's been set manually.
        if 'db_index' not in kwargs:
            kwargs['db_index'] = True
        super(SmileyCodeField, self).__init__(*args, **kwargs)


# Allow South to handle those fields smoothly
try:
    from south.modelsinspector import add_introspection_rules

    # For a normal BBCodeTextField, the add_rendered_field attribute is always True,
    # which means that the no_rendered_field arg will always be True in a frozen BBCodeTextField,
    # which is what we want. The use of this flag will tell South not to make the _rendered
    # fields again.
    add_introspection_rules(rules=[((BBCodeTextField,),
                                    [],
                                    {'no_rendered_field': ('add_rendered_field',
                                                           {})})],
                            patterns=['precise_bbcode\.fields\.BBCodeTextField'])

    # SmileyCodeField
    add_introspection_rules([], ['^precise_bbcode\.fields\.SmileyCodeField'])
except ImportError:  # pragma: no cover
    pass
