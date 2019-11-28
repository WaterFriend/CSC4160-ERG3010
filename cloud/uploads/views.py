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


@csrf_exempt
def upload(request,doctorID):  #(request, userID)
    if request.method == "POST":
        check_box   = request.POST.getlist('check_box')
        
        fName      = request.POST.get('firstName')
        lName       = request.POST.get('lastName')
        gender      = request.POST.get('gender')
        race        = request.POST.get('race')
        ethnicity   = request.POST.get('ethnicity')
        status      = request.POST.get('status')
        age         = request.POST.get('age')
        dID         = Doctor.objects.get(dID=doctorID)
        
        message = "You should agree with the upload privacy of Cancer Dection System!"
        if check_box:
            if fName != "" and lName != "":                                                     #check if user doesn't provide patient's full name 
                if gender != "":                                                                #check if user doesn't provide patient's gender 
                    if "@" in userEmail:                                                        #check if this is a formal E-mail formate
                        if RegInfo.objects.filter(reg_id=userEmail).exists() == False:          #check if the account had existed
                            if password == repPassword:                                         #check if the two passwords are differents 

                                if accountType == "Student":
                                    sid = "0" + time.strftime("%Y%m%d%H%M%S", time.localtime()) 
                                    #print(sid)
                                    Reg = RegInfo.objects.create(reg_id=userEmail, reg_password=password)
                                    Stu = Student.objects.create(stu_id=sid, stu_email=userEmail, reg=Reg)
                                    return redirect('../stu/editor/%s' %sid)
                                
                                elif accountType == "University":
                                    uid = "1" + time.strftime("%Y%m%d%H%M%S", time.localtime()) 
                                    #print(uid)
                                    Reg = RegInfo.objects.create(reg_id=userEmail, reg_password=password)
                                    Uni = University.objects.create(uni_id=uid, uni_email=userEmail, reg=Reg)
                                    return redirect('../uni/editorCreate/%s' %userEmail)  

                                elif accountType == "Guardian":
                                    gid = "2" + time.strftime("%Y%m%d%H%M%S", time.localtime())
                                    #print(gid)
                                    Reg = RegInfo.objects.create(reg_id=userEmail, reg_password=password)
                                    Gua = Guardian.objects.create(guardian_id=gid, guardian_email=userEmail, reg=Reg) 
                                    return redirect('../guardian/editor/%s' %gid)                                                      
                            else:
                                message = "Your second password is not match, please try again."
                        else:
                            message = "The account is already exist!"
                    else:
                        message = "Please enter correct E-mail format."
                else:
                    message = "Please provide patient's gender!"
            else:
                message = "Please provide patient's full name!"
        return render(request, 'reg/register.html', {"message": message})
    return render(request, 'reg/register.html')

