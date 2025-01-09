from django import forms
from django.contrib.auth.forms import UserCreationForm

from Event_App.models import Customer_Profile,Event_Booking,User

#-----------------------------------UserRegistration___________________________________________________________________________

class User_Reg(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class Customer_Reg(forms.ModelForm):
    class Meta:
        model = Customer_Profile
        exclude = ('user',)

class DateInput(forms.DateInput):
    input_type = 'Date'

class Event_Reg(forms.ModelForm):
    Event_Date = forms.DateField(widget=DateInput)
    class Meta:
        model = Event_Booking
        exclude = ('Approval_Status','user',)



class Edit_Profile_form(forms.ModelForm):
    class Meta:
        model = Customer_Profile
        exclude = ('user',)




from django import forms
from .models import Event, User, Customer_Profile, Event_Booking


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date']