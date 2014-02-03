from django import template

register = template.Library()

@register.filter(name='getktv')
def getktv(value, arg):
	return value.get(arg, '')
