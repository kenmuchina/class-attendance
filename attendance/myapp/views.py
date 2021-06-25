from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Attended_class
from .forms import LoginForm

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def login(request):
    if request.method == "POST":

        form = LoginForm(request.POST)

        print('Got the post request')
        # Check if it's valid
        if form.is_valid():
            # Access users details in each field
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            # Instantiate a student
            student = Attended_class(username=username, email=email, password=password)

            # Save the user to the attended class model
            student.save()

            # Redirect users to the class
            return redirect('/attendees/', {'username': username})
        else:
            return HttpResponseRedirect('login-error/')

        
    else:
        form = LoginForm()
    
    return render(request, 'myapp/login.html', {'form': form})
    
def attendees(request):
    students_who_attended = Attended_class.objects.all()

    return render(request, 'myapp/attendees.html', { 'students': students_who_attended  })


