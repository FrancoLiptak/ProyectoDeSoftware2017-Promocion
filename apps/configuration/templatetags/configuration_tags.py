from django.template import Library
from apps.configuration.models import Configuration
register = Library()

@register.simple_tag()
def title():
    return Configuration.objects.all()[:1].get().title

@register.simple_tag()
def description():
    return Configuration.objects.all()[:1].get().description

@register.simple_tag()
def email():
    return Configuration.objects.all()[:1].get().email

@register.simple_tag()
def items_per_page():
    return Configuration.objects.all()[:1].get().items_per_page

@register.simple_tag()
def phone():
    return Configuration.objects.all()[:1].get().phone

@register.simple_tag()
def address():
    return Configuration.objects.all()[:1].get().address