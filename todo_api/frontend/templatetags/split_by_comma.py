from django import template

register = template.Library()

@register.filter(name='splitbycomma')
def splitbycomma(value,arg):
    return value.split(",")