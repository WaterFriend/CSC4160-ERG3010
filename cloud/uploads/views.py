#-*- conding:utf-8 -*-
import time
from django.contrib              import auth
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models  import User
from django.http                 import HttpResponseRedirect, HttpResponse
from django.shortcuts            import render, redirect
from django.contrib              import messages

# Create your views here.
from .models        import Patient
from login.models   import Doctor
# from .forms import InfoForm


