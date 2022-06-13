from django import template
register = template.Library()

# @register.filter(name='place')
# def place(field, text):
#     return field.as_widget(attrs={"placeholder":text})
#

@register.filter(name='place')
def place(field, text):
    return field.as_widget(attrs={"placeholder":text,'class':'form-control'})