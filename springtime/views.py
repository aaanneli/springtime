from django.shortcuts import render
from springtime.forms import UserForm, ReviewForm, SelectDateForm, SelectSlotForm
from springtime.models import Trampoline, Category, Review, Booking, SelectDate
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from datetime import datetime
from django.contrib.auth.decorators import login_required

def index(request):
    # Return the index page
    return render(request, 'springtime/index.html', {})

# If the username typed in the box is 'taken' (exists already), 
# display an error message on screen.
def validate_username(request):
	username = request.GET.get('username', None)
	# Assigns 'is_taken' = a check if the username already exists.
	data = {
		'is_taken': User.objects.filter(username__iexact=username).exists()
	}
	# If 'is_taken' is true, the username exists already, display error message.
	if data['is_taken']:
		data['error_message'] = 'A user with this username already exists.'
	return JsonResponse(data)

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

# Shows trampolines.
def trampolines(request):
	# Create context dictionary.
    context_dict = {}
    categories = Category.objects.all()
    trampolines = Trampoline.objects.all()
    context_dict ['categories'] = categories
    context_dict ['trampolines'] = trampolines
    # Render and return trampolines page.
    return render(request, 'springtime/trampolines.html', context_dict)

# Display categories.
def show_category(request, category_name_slug):
	# Create a context dictionary to pass to the template rendering engine.
    context_dict = {}
    try:
    	# If can't find a category name slug with the given name, 
    	# the .get() method raises DoesNotExist exception.
    	# If it finds it, returns one model instance.
        category = Category.objects.get(slug=category_name_slug)
        # Retrieves all associated trampolines.
        trampolines = Trampoline.objects.filter(category=category)
        # Adds result list to template context under name trampolines.
        context_dict['trampolines'] = trampolines
        # Add category to object from the database to context dictionary. 
        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['trampolines'] = None

    # Render category page and return to client.
    return render(request, 'springtime/category.html', context_dict)

def user_login(request):
	# If request is HTTP POST, try to pull out the relevant information.
	if request.method == 'POST':
		# Gather username and password provided by user in login form.
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

# Display form required to add a new review and save details from it.
@login_required
def add_review(request):
    form = ReviewForm()
    reviews = Review.objects.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)

		# If form is valid, save details, else return errors.
		# userID is set to be the current user, review time is the time now. 
        if form.is_valid():
			review = form.save(commit=False)
			review.time = datetime.now()
			review.userID = request.user
			review.save()
			return index(request)
        else:
		print(form.errors)
	# Render and return review page.
    return render(request, 'springtime/add_review.html', {'form': form, 'reviews' : reviews})

# Displays booking form and saves data from it.
@login_required
def bookings(request):
    form = SelectDateForm

    if request.method == 'POST':
        form = SelectDateForm(request.POST)

        # If the form is valid, save the details. If not valid, print errors.
        if form.is_valid():
            form.save(commit=False)
            return select_timeslot(request, form)
        else:
            print(form.errors)

    # Render and return bookings page.
    return render(request, 'springtime/bookings.html', {'form': form})

# Allows users to select a timeslot for a booking.
def select_timeslot(request, dateform):
    bookings = Booking.objects.all()
    
    slotchoices = ("09", "10", "11", "12", "13", "14", "15", "16", "17")
    
    
    Times = []
    HourTimes = {}

    print "Bookings:" 
    for bking in bookings:
        print bking.getStartTime()
        Times.append(bking.getStartTime().strftime("%Y-%m-%d"))
        if bking.getStartTime().strftime("%Y-%m-%d") not in HourTimes.keys():
            HourTimes[bking.getStartTime().strftime("%Y-%m-%d")] = []

        HourTimes[bking.getStartTime().strftime("%Y-%m-%d")].append([(bking.getStartTime().strftime("%H"))])

        HourTimes[bking.getStartTime().strftime("%Y-%m-%d")].append((bking.getStartTime().strftime("%H")))

         
    print "Hour Times = " 
    print HourTimes
        
        
    chosendate = str(datetime.strptime(str(dateform.cleaned_data['date']), '%Y-%m-%d'))[0:10]
    
    for t in Times:
        print t[3::]
    
    timeslotform = SelectSlotForm
    
    if request.method == 'POST':
        timeslotform = SelectSlotForm(request.POST)

        # If form is valid, save details. Return 'successful booking' page.
        # Else return errors.
        if timeslotform.is_valid():
            timeslotform.save(commit=True)
            return successful_booking(request, timeslotform)
        else:
            print(timeslotform.errors)
<<<<<<< HEAD
    # Return and return book_slot page depending on the context.
    return render(request, 'springtime/book_slot.html', {'bookings' : bookings, 'chosendate':chosendate, 'selectslotform':timeslotform, 'existingtimes':Times, 'slots':slotchoices})
=======

    return render(request, 'springtime/book_slot.html', {'bookings' : bookings, 'chosendate':chosendate, 'selectslotform':timeslotform, 'existingtimes':HourTimes, 'slots':slotchoices})
>>>>>>> fc01e6ef07167a5764c8bb29b774b716a798dd20


# Render and return registration complete page.
def user_registered(request):
	return render(request, 'springtime/registration_complete.html', {})

# If user is logged in, log them out and redirect to index page.
@login_required
def user_logout(request):
	logout(request)
	# Redirect user to homepage.
	return HttpResponseRedirect(reverse('index'))

# If user is logged in, render and return password change page.
@login_required
def password_change(request):
	return render(request, 'registration/password_change.html', {})

# If user is logged in and has changed password, display password change complete page.
@login_required
def password_change_done(request):
	return render(request, 'registration/password_change_done.html', {})

# Renders and returns Contact Us page.
def contact_us(request):
	return render(request, 'springtime/contact_us.html', {})

