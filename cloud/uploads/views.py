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


def upload(request):
    if request.method == "POST":
        firstName   = request.POST.get('firstName')
        lastName    = request.POST.get('lastName')
        gender      = request.POST.get('gender')
        race        = request.POST.get('race')
        ethnicity   = request.POST.get('ethnicity')
        status      = request.POST.get('status')
        agree       = request.POST.get('age')



        userEmail = request.POST.get('userEmail')
        password = str(request.POST.get('password'))
        repPassword = str(request.POST.get('reppassword'))
        message = "You should agree with the privacy of Exam and Application System!"
        if check_box:
            if accountType != "I am" and accountType != None:           
                if userEmail != "" and password != "" and repPassword != "":                    #check if user doesn't complete his/her form
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
                    message = "Please complete the forms of Email and password!"
            else:
                message = "Please select your account type!"
        return render(request, 'reg/register.html', {"message": message})
    return render(request, 'reg/register.html')
