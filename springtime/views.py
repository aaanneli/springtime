from django.shortcuts import render
from django.http import HttpResponse
from springtime.forms import UserForm

def index(request):
    #This should change to return the index page
    return render(request, 'springtime/main.html')

def register(request):
	# Boolean value tells template whether registration was successful. 
	# Set to false initially.
	registered = False

	# If HTTP POST, process form data.
	if request.method == 'POST':
		# Grab information from raw form information. 
		user_form = UserForm(data=request.POST)

		#If form is valid...
		if user_form.is_valid():
			#Saves user's form data to database.
			user = user_form.save()

			# Hash password with set_password method.
			user.set_password(user.password)
			user.save()

			# Update variable to indicate that template registration was success.
			registered = True

		else:
			# Invalid form, print problems to terminal.
			print(user_form.errors)
	else:
		# Not a HTTP POST, so render form using ModelForm instance.
		user_form = UserForm()

	# Render the template depending on the context.
	return render(request, 'springtime/register.html', 
		{'user_form': user_form,
		 'registered': registered})

