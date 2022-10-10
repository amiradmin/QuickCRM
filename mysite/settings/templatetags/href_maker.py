# order_filters.py
from django import template
register = template.Library()

@register.filter(name='href')
def href(value):
    print(value)
    if value:

        result = value[1:]
        print(result)
        return result

# @register.filter
# def href(value):
#     print(value)
#     result = value.split('#')
#     return result
