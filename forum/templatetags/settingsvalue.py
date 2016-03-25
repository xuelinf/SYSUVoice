from django import template
from SYSUVoice import settings
from SYSUVoice import conf

register = template.Library()
__author__ = 'Selfboot'

'''
usage:
first
    {% load settingsvalue %}
then
   {% settings_value "MAX_UPLOAD_SIZE" %}
   or
    {% settings_value "logoname" %}

'''


@register.simple_tag
def settings_value(name):
    return getattr(settings, name, "")


@register.simple_tag
def conf_value(name):
    return getattr(conf, name, "")
