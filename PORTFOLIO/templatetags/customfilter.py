from django import template

register = template.Library()

@register.filter(name='slice')
def slice(value, arg):
    return value[:arg]
