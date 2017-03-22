from django import forms
from django.contrib.auth.models import User
from springtime.models import UserProfile, Review, Booking

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class ReviewForm(forms.ModelForm):
    content = forms.CharField(max_length=300,
                                help_text="Tell us what you thought:")
    rating = forms.IntegerField(help_text="Give a rating:", min_value=1, max_value=5)

    class Meta:
        model = Review
        fields = ('content', 'rating')
        
        
class BookingForm(forms.ModelForm):
    date = forms.DateField(help_text="Date", widget = forms.SelectDateWidget(years=[2017, 2018]))
    details = forms.CharField(max_length=500, help_text="Do you have any special requirements?")
    
    class Meta:
        model = Booking
        fields = ('date', 'details')