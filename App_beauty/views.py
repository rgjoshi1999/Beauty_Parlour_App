from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import ImageForm, SignUpForm, Feedbackform, BookAppointmentForm
from .models import Image, Appointment, Feedback


# Create your views here.
def signout(request):
    logout(request)
    return redirect("home")

def home(request):
    return render(request,'home.html')

def About(request):
    return render(request,'About.html')

def Gallery(request):
    return render(request,'Gallery.html')

def customer_photos(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'customer_photos.html', {'img':img,'form':form})

def Location(request):
    return render(request,'Location.html')

def Services(request):
    return render(request,'Services.html')

def hair(request):
    return render(request,'hair.html')

def skin(request):
    return render(request,'skin.html')

def makeup(request):
    return render(request,'makeup.html')

def beauty_com(request):
    return render(request,'beauty_com.html')

def book_appointment(request):
    return render(request,'book_appointment.html')

def cut_all(request):
    return render(request,'cut_all.html')

def hair_color(request):
    return render(request,'hair_color.html')

def hair_treatment(request):
    return render(request,'hair_treatment.html')

def signin(request):
    return render(request,'signin.html')


'''
def book_appointment(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        appointment_form = AppointmentForm(request.POST)
        if customer_form.is_valid() and appointment_form.is_valid():
            customer = customer_form.save()
            appointment = appointment_form.save(commit=False)
            appointment.customer = customer
            appointment.save()
            return redirect('appointment_success')
    else:
        customer_form = CustomerForm()
        appointment_form = AppointmentForm()
    return render(request, 'book_appointment.html', {'customer_form': customer_form, 'appointment_form': appointment_form})
'''
def book_appointment(request):
    if request.method == 'POST':
        form = BookAppointmentForm(request.POST)
        if form.is_valid():
            # And then redirect to a success page or display a success message
            return redirect('appointment_confirmation')  # Replace 'success_page' with the URL name of your success page
    else:
        form = BookAppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})



def signin(request):
            if request.method == 'POST':
                form = AuthenticationForm(request, request.POST)
                if form.is_valid():
                    user = form.get_user()
                    login(request, user)
                    return redirect('book_appointment')
            else:
                form = AuthenticationForm()
            return render(request, 'signin.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)  # Use SignUpForm here
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_appointment')
    else:
        form = SignUpForm()  # Use SignUpForm here
    return render(request, 'signup.html', {'form': form})

def appointment_confirmation(request):
    # Logic for confirming the appointment and sending confirmation email/WhatsApp
    return render(request, 'appointment_confirmation.html')


def thank_you(request):
    # If you want to pass any context data to the template, you can do so here
    context = {
        'name': 'User',  # Replace 'User' with the actual name if available
    }
    return render(request, 'thank_you.html', context)

def feedback(request):
    if request.method == "POST":
        fd = Feedbackform(request.POST)
        if fd.is_valid():
            if not request.user.is_authenticated:
                return redirect('SignIn')
            fd.save()
            return redirect("feedback")
    else:
        fd = Feedbackform()
    show = Feedback.objects.all()
    return render(request, 'feedback.html',{'feedback': fd,'show': show})

def showfeedback(request):
    show = Feedback.objects.all()
    return render(request,'reviews.html',{'show':show})
