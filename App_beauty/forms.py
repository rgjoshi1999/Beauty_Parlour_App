from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Feedback
from django.forms import DateTimeInput


from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        labels = {'photo':''}


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    mobile_number = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(max_length=254,  required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, required=True)
    username = forms.CharField(max_length=40, required=True)


    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'mobile_number', 'email', 'password1', 'password2')



class TimeInput(forms.TimeInput):
    input_type = 'time'

class BookAppointmentForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name', widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    phone_number = forms.CharField(max_length=15, label='Phone Number', widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'}))
    appointment_date = forms.DateField(label='Appointment Date', widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'Select appointment date'}))
    appointment_time = forms.TimeField(label='Appointment Time', widget=forms.TimeInput(attrs={'type': 'time', 'placeholder': 'Select appointment time'}))
    services = forms.ChoiceField(choices=[('service1', 'Service 1'), ('service2', 'Service 2'), ('service3', 'Service 3')], label='Select Service')

class Feedbackform(forms.ModelForm):
    class Meta:
        model=Feedback
        fields = ['username','feedback']