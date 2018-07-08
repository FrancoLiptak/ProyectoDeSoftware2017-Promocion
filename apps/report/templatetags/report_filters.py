from django.template import Library
register = Library()

@register.filter
def weeks(value):
    return float(value)/7

@register.filter
def ages(value):
    return float(value)/365