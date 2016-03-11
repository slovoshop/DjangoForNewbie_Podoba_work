
from django import template

register = template.Library()

@register.filter
def nice_username(user):
	"""Show first and last name of user"""

	try:
		if user.first_name  or user.last_name:
			# name = user.get_full_name
			name = user.first_name + " " + user.last_name + " "
		else:
			name = user.username + " " 

	except ValueError:
		name = "We have problem with user object!"
		
	return name 

	
	
