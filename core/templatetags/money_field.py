from django import template

register = template.Library()
@register.filter(name='format_money')
def format_money(value):
    if value is None:
        return '0'
    
    return str(value).split('.')[0]