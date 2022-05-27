from django import template

register = template.Library()

@register.filter()
def to_list(value):
    list1=[]
    list1[:0]=value
    return list1


# @register.filter(name='payment')
# def payment(id):
#     """Convert a 10 character string into (xxx) xxx-xxxx."""
#
#     return 'paid:' + id
#

