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
                                help_text="Tell us about your experience:")
    rating = forms.IntegerField(help_text="Rate your experience:", min_value=1, max_value=5)
    userID = User.username

    class Meta:
        model = Review
        fields = ('userID', 'content', 'rating')


class BookingForm(forms.ModelForm):
    date = forms.DateField(help_text="Chose a date you would like to come for a jump", widget = forms.SelectDateWidget(years=[2017, 2018]))
    details = forms.CharField(max_length=150, help_text="Please inform us of any special requirements you may have:")

    class Meta:
        model = Booking
        fields = ('date', 'details')