# order_filters.py
from django import template
register = template.Library()

@register.filter(name='phone_number')
def phone_number(number):
    """Convert a 10 character string into (xxx) xxx-xxxx."""
    first = number[0:3]
    second = number[3:6]
    third = number[6:10]
    return '(' + first + ')' + ' ' + second + '-' + third

@register.filter
def order_by(queryset,name='order_by'):
    return queryset.order_by('-id')


