from django import forms
from django.contrib.auth.models import User
from springtime.models import UserProfile, Review, Booking, SelectDate
from django.utils import timezone

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class ReviewForm(forms.ModelForm):
    content = forms.CharField(max_length=300,
                                help_text="Tell us about your experience:")
    rating = forms.IntegerField(help_text="Rate your experience:", min_value=1, max_value=5)
    #userID = User
    reviews = Review.objects.all()

    class Meta:
        model = Review
        fields = ('content', 'rating')


class SelectDateForm(forms.ModelForm):
    date = forms.DateField(help_text="Choose a date you would like to come for a jump", widget = forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"), years=[2017], months={3:"March", 4:"April", 5:"May"}))

    class Meta:
        model = SelectDate
        fields = ('date',)
        
        
class SelectSlotForm(forms.ModelForm):
    SLOTS = (('1', '09:00 - 10:00'), ('2', '10:00 - 11:00'), ('3', '11:00 - 12:00'), ('4', '12:00 - 13:00'), ('5', '13:00 - 14:00'), ('6', '14:00 - 15:00'), ('7', '15:00 - 16:00'), ('8', '16:00 - 17:00')) # '0' means unavailable
    slots = forms.ChoiceField(widget=forms.RadioSelect, choices=SLOTS)
    
    class Meta:
        model = Booking
        fields = ('slots',)