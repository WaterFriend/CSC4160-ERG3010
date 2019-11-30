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
from .forms         import PatientForm, PForm
from .models        import Patient
from login.models   import Doctor
# from .forms import InfoForm

@csrf_exempt
def uploadPage(request, doctorID):
    if request.method == "POST":
        fName       = request.POST.get('fName')
        lName       = request.POST.get('lName')
        gender      = request.POST.get('gender')
        race        = request.POST.get('race')
        ethnicity   = request.POST.get('ethnicity')
        pstatus      = request.POST.get('pstatus')
        remark      = request.POST.get('remark', 'None')
        age         = request.POST.get('age')
        imgURL      = request.POST.get('imgURL')
        doc = Doctor.objects.get(dID = doctorID)
        print(request.POST)

        if fName != "" and lName != "":                                                         #check if user doesn't provide patient's full name
            if gender != "":                                                                #check if user doesn't provide patient's gender 
                if race != "":                                                              #check if user doesn't provide patient's race
                    if ethnicity != "":                                                     #check if user doesn't provide patient's ethnicity
                        if pstatus != "":                                                    #check if user doesn't provide patient's status
                            if age != None:                                                 #check if user doesn't provide patient's age
                                patientID = "p" + time.strftime("%Y%m%d%H%M%S", time.localtime()) 
                                #print(sid)
                                print(patientID, fName, lName, gender, race, ethnicity, pstatus, age)
                                patient = Patient.objects.create(pID=patientID, pFName=fName, pLName=lName, pGender=gender,
                                                                    pRace=race, pEthnicity=ethnicity, pStatus=pstatus, pAge=age, pRemark=remark, pImage=imgURL, dID=doc)                                            
                                print("update database succeed!!!!!!!!!!!!!")
                                message = "update database succeed!!!!!!!!!!!!!"
                                return redirect('../home/%s' %doctorID)
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
            message = "Please provide patient's full name!"
    else:
        return render(request, 'upload/upload.html', {"doctorID": doctorID})
    
    return HttpRepsonse('FAIL!!!!!')


@csrf_exempt
def upload(request):  #(request, userID)
    if request.method == "POST":
        fName       = request.POST.get('firstName')
        lName       = request.POST.get('lastName')
        gender      = request.POST.get('gender')
        race        = request.POST.get('race')
        ethnicity   = request.POST.get('ethnicity')
        pstatus     = request.POST.get('pstatus')
        remark      = request.POST.get('remark', 'None')
        age         = request.POST.get('age')
        imgURL      = request.POST.get('imgURL')
        doctorID    = request.POST.get('doctorID')
        
        if fName != "" and lName != "":                                                         #check if user doesn't provide patient's full name
            if Patient.objects.filter(Q(pFName=fName) | Q(pLName=lName)).exists() == False:     #check if the patient had existed  
                if gender != "":                                                                #check if user doesn't provide patient's gender 
                    if race != "":                                                              #check if user doesn't provide patient's race
                        if ethnicity != "":                                                     #check if user doesn't provide patient's ethnicity
                            if status != "":                                                    #check if user doesn't provide patient's status
                                if age != None:                                                 #check if user doesn't provide patient's age
                                    patientID = "p" + time.strftime("%Y%m%d%H%M%S", time.localtime()) 
                                    #print(sid)
                                    patient = Patient.objects.create(pID=patientID, pFName=fName, pLName=lName, pGender=gender,
                                                                        pRace=race, pEthnicity=ethnicity, pStatus=pstatus, pAge=age, pRemark=remark, pImage=imgURL, dID=doctorID)                                            
                                    print("update database succeed!!!!!!!!!!!!!")
                                    message = "update database succeed!!!!!!!!!!!!!"
                                    return redirect('../home/%s' %doctorID)
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
    
    return HttpRepsonse('FAIL!!!!!')

