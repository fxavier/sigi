import datetime
from django import template

register = template.Library()


@register.simple_tag
def tempo_actual():
    return datetime.datetime.now().strftime('%H:%M:%S')
