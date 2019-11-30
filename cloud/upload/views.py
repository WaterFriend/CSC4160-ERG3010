#-*- conding:utf-8 -*-
import time
from django.contrib               import auth
from django.contrib.auth.hashers  import make_password,check_password
from django.contrib.auth.models   import User
from django.views.decorators.csrf import csrf_exempt
from django.http                  import HttpResponseRedirect, HttpResponse
from django.shortcuts             import render, redirect
from django.contrib               import messages
from django.db.models             import Q

# Create your views here.
from .forms import PatientForm, PForm
from .models        import Patient
from login.models   import Doctor
# from .forms import InfoForm


def uploadPage(request, doctorID):
    return render(request, 'upload/upload.html', {"doctorID": doctorID})


@csrf_exempt
def upload(request,doctorID):  #(request, userID)
    if request.method == "POST":
        fName       = request.POST.get('firstName')
        lName       = request.POST.get('lastName')
        gender      = request.POST.get('gender')
        race        = request.POST.get('race')
        ethnicity   = request.POST.get('ethnicity')
        status      = request.POST.get('status')
        remark      = request.POST.get('remark', 'None')
        age         = request.POST.get('age')
        imgURL      = request.POST.get('imgURL')
        
        message = "You should agree with the upload privacy of Cancer Dection System!"
        if fName != "" and lName != "":                                                         #check if user doesn't provide patient's full name
            if Patient.objects.filter(Q(pFName=fName) | Q(pLName=lName)).exists() == False:     #check if the patient had existed  
                if gender != "":                                                                #check if user doesn't provide patient's gender 
                    if race != "":                                                              #check if user doesn't provide patient's race
                        if ethnicity != "":                                                     #check if user doesn't provide patient's ethnicity
                            if status != "":                                                    #check if user doesn't provide patient's status
                                if age != None:                                                 #check if user doesn't provide patient's age
                                    if accountType == "Student":
                                        patientID = "p" + time.strftime("%Y%m%d%H%M%S", time.localtime()) 
                                        #print(sid)
                                        patient = Patient.objects.create(pID=patientID, pFName=fName, pLName=lName, pGender=gender,
                                                                            pRace=race, pEthnicity=ethnicity, pStatus=status, pAge=age, pRemark=remark, pImage=imgURL, dID=doctorID)                                            
                                        #return redirect('../stu/editor/%s' %sid)
                                else:
                                    message = "Please provide patient's age!"                                                   
                            else:
                                message = "Please provide patient's status!"
                        else:
                            message = "Please provide patient's ethnicity!"
                    else:
                        message = "Please provide patient's race!"
                else:
                    message = "Please provide patient's gender!"
            else:
                message = "The patient had already exist!"
        else:
            message = "Please provide patient's full name!"
    
    return render(request, 'upload/upload.html')

