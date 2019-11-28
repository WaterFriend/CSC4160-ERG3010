from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import UserProfile

def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is taken!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is taken!')
                return redirect('register')
            else:   
                user = User.objects.create_user(username=username, password=password1,email=email, first_name = firstname, last_name = lastname)
                user.save()
                print("User created!")
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match!')
            return redirect('register')


    else:
        return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']

        user = auth.authenticate(username=username, password=password1)

        if user is not None:
            auth.login(request, user)
            return redirect('result_list')
        else:
            messages.info(request, "Username or password do not exist.")
            return redirect('login')

    else:
        return render(request, 'login.html')

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
