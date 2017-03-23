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
    userID = User
    reviews = Review.objects.all()

    class Meta:
        model = Review
        fields = ('userID', 'content', 'rating')


class BookingForm(forms.ModelForm):
    date = forms.DateField(help_text="Choose a date you would like to come for a jump", widget = forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"), years=[2017], months={1:"March", 2:"April", 3:"May"}))
    SLOTS = (('1', '09:00 - 10:00'), ('2', '10:00 - 11:00'), ('0', '11:00 - 12:00'), ('4', '12:00 - 13:00'), ('5', '13:00 - 14:00'), ('0', '14:00 - 15:00'), ('7', '15:00 - 16:00'), ('6', '16:00 - 17:00'))
    slots = forms.ChoiceField(widget=forms.RadioSelect, choices=SLOTS)

    class Meta:
        model = Booking
        fields = ('date',)