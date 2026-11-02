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


@register.filter(name='github_username')
@stringfilter
def github_username(value):
    """Extract username from GitHub URL or return value if it's already a username."""
    if not value:
        return value
    # Remove trailing slash
    value = value.rstrip('/')
    # If it's a full URL
    if value.startswith('https://github.com/'):
        return value.replace('https://github.com/', '')
    elif value.startswith('http://github.com/'):
        return value.replace('http://github.com/', '')
    elif value.startswith('github.com/'):
        return value.replace('github.com/', '')
    # If it already contains a path (username/repo format)
    elif '/' in value:
        return value.split('/')[0]
    return value


@register.filter(name='linkedin_username')
@stringfilter
def linkedin_username(value):
    """Extract username from LinkedIn URL or return value if it's already a username."""
    if not value:
        return value
    # Remove trailing slash
    value = value.rstrip('/')
    # If it's a full URL
    if value.startswith('https://www.linkedin.com/in/'):
        return value.replace('https://www.linkedin.com/in/', '')
    elif value.startswith('https://linkedin.com/in/'):
        return value.replace('https://linkedin.com/in/', '')
    elif value.startswith('http://www.linkedin.com/in/'):
        return value.replace('http://www.linkedin.com/in/', '')
    elif value.startswith('http://linkedin.com/in/'):
        return value.replace('http://linkedin.com/in/', '')
    elif value.startswith('www.linkedin.com/in/'):
        return value.replace('www.linkedin.com/in/', '')
    elif value.startswith('linkedin.com/in/'):
        return value.replace('linkedin.com/in/', '')
    # If it already contains a path
    elif '/' in value:
        parts = value.split('/')
        return parts[-1] if parts[-1] else parts[-2]
    return value
