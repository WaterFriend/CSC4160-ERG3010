import time
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

from upload.models      import Patient


@csrf_exempt
def result_list(request, doctorID):
    if request.method == "GET":
        if 'search' in request.GET:
            patientList = Patient.objects.all()
            firstName = request.POST.get('firstname')
            lastName = request.POST.get('lastname')
            gender = request.POST.get('gender')
            age = request.POST.get('age')
            
            print("!!!!!firstname: ", firstName, " lastname: ", lastName, " gender: ", gender, " age: ", age)

            patientList = patientList.filter(dID=doctorID)
            #print("first print: ", patientList)
            if firstName != "" and firstName != None:
                patientList = patientList.filter(pFName=firstName)
            if lastName != "" and lastName != None:
                patientList = patientList.filter(pLName=lastName)
            if gender != "" and gender != None:
                patientList = patientList.filter(pGender=gender)
            if age != None:
                patientList = patientList.filter(pAge=age)
            
            #print("second print: ", patientList)

            content = {
                'uploadLink'  : "../upload/" + doctorID,
                'patient'     : patientList,
            }
            return render(request, 'home.html', content)
        else:
            patientList = Patient.objects.all()
            content = {
                'uploadLink'  : "../upload/" + doctorID,
                'patient'     : patientList.filter(dID=doctorID),
            }
            return render(request, 'home.html', content)  
    elif request.method == "POST":
        if 'logout' in request.POST:   
            logout(request) 
            return redirect('../login/login')
        # elif 'upload' in request.POST:
        #     patientID
        #     return redirect('../result/%s' %doctorID)
