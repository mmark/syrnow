from __future__ import unicode_literals
from django import template

register = template.Library()


@register.filter
def check_type(obj, object_type):

    try:
        type = obj.__class__.__name__

        return type.lower() == str(object_type).lower()
    except:
        pass

    return False


@register.filter
def field_type(field, field_type):

    return check_type(field.field.widget, field_type)
