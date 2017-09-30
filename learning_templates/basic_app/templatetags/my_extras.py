from django import template

register = template.Library()

@register.filter(name='cutting')
def cutting(value,args):
	"""This cut out all values from the args"""
	return value.replace(arg,'')

# register.filter('cut':cut)
