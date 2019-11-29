from django.shortcuts               import render, redirect, render_to_response
from django.views.generic           import TemplateView, FormView, ListView
from django.core.files.storage      import FileSystemStorage
from django.contrib.staticfiles     import finders
from django.contrib.auth            import logout
from django.contrib                 import messages
from django.contrib.auth.decorators import login_required
from django.db.models               import Q
from django.views.decorators.csrf   import csrf_exempt
import json
import time
import os



@csrf_exempt
def result_list(request, doctorID):
    if request.method == "GET":
        content = {
            'homeLink'    : "../" + doctorID,
            'loginLink'   : "../login/login",
            'uploadLink'  : "../upload/" + doctorID,
        }
        return render(request, 'home.html', content)  
    elif request.method == "POST":   
        logout(request) 
        return redirect('../login/login')
