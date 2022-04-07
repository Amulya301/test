from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .forms import SignUpForm


# Create your views here.
def signUpAs(request):
    return render(request, 'accounts/sign-up-as.html')


def tuteeSignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('website:index')
        else:
            return render(request, 'accounts/tutee-sign-up.html', {
                'error_message': 'Error'
            })
    else:
        form = SignUpForm()
        return render(request, 'accounts/tutee-sign-up.html')


def instructorSignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            current_user = User.objects.get(username=username)
            current_user.is_staff = True
            current_user.save()

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('website:index')
        else:
            return render(request, 'accounts/instructor-sign-up.html', {
                'error_message': 'Error'
            })
    else:
        form = SignUpForm()
        return render(request, 'accounts/instructor-sign-up.html')


def signIn(request):
    return None
