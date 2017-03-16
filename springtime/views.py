from django.shortcuts import render
from springtime.forms import UserForm
from springtime.models import Trampoline
from springtime.models import Category
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    #Return the index page
    return render(request, 'springtime/index.html')

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

def trampolines(request):
    context_dict = {}
    categories = Category.objects.all()
    context_dict['categories'] = categories
    return render(request, 'springtime/trampolines.html', context_dict)

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        trampolines = Trampoline.objects.filter(category=category)
        context_dict['trampolines'] = trampolines
        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['trampolines'] = None
        return render(request, 'springtime/category.html', context_dict)

def user_login(request):
	# If request is HTTP POST, try to pull out the relevant information.
	if request.method == 'POST':
		# Gather usernamd and password provided by user in login form.
		username = request.POST.get('username')
		password = request.POST.get('password')

		# See if username/password combination is valid.
		user = authenticate(username=username, password=password)

		# If we have User object, the details are correct.
		# If None, no user with matching credentials.
		if user:
			if user.is_active:
				# If account is valid and active, log the user in.
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				# An inactive account was used - no logging in.
				return HttpResponse("Your Springtime account is disabled.")

		else:
			# Bad login details provided, can't log user in.
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")

		# The request is not a HTTP POST, so display the login form.
	else:
		return render(request, 'registration/login.html', {})


@login_required
def user_logout(request):
	logout(request)
	# Return user to homepage.
	return HttpResponseRedirect(reverse('index'))

def bookings(request):
	return render(request, 'springtime/bookings.html', ())

