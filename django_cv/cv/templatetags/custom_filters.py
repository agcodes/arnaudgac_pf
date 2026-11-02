from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='split')
@stringfilter
def split(value, delimiter=';'):
    """Split a string by delimiter and return a list."""
    return value.split(delimiter)


@register.filter(name='strip')
@stringfilter
def strip(value):
    """Remove leading and trailing whitespace."""
    return value.strip()
