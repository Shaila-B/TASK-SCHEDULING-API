from django import template

register = template.Library()

@register.filter(name='get_dict_value')
def get_dict_value(value, arg):
    if arg in value :
        return value[arg]
    else :
        return ''