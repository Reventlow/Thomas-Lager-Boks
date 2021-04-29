from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home_auth(request):
    return  render(request, 'home_auth.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return  redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.error(request, ("Forkert brugernavn og/eller adgangskode"))
            return  redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.error(request, ("Du er logget ud"))
    return redirect('login')

