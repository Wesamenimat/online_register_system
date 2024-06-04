from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, RegistrationForm
from .models import College, Major, Subject, StudentSubject
from django.contrib.auth import logout

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signin_signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'signin_signup.html', {'form': form})

@login_required
def register(request):
    if request.method == 'POST':
        college_name = request.POST.get('college')
        major_name = request.POST.get('major')
        subject_name = request.POST.get('subject')
        
        college = College.objects.get(name=college_name)
        major = Major.objects.get(name=major_name)
        
        subject, created = Subject.objects.get_or_create(name=subject_name, major=major)
        
        StudentSubject.objects.create(user=request.user, subject=subject)
        
        return redirect('schedule')
    else:
        form = RegistrationForm()
        colleges = College.objects.all()
        return render(request, 'register.html', {'form': form, 'colleges': colleges})

@login_required
def schedule(request):
    subjects = StudentSubject.objects.filter(user=request.user)
    return render(request, 'schedule.html', {'subjects': subjects})
