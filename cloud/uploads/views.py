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
def upload(request):  #(request, userID)
    if request.method == "POST":
        message = "You should agree with the upload privacy of Cancer Dection System!"
        check_box = request.POST.getlist('check_box')
        stu = Student.objects.get(stu_id=userID)
        stu.stu_fname = request.POST.get('firstName')
        stu.stu_lname = request.POST.get('lastName')
        if request.POST.get('firstName') != "" and request.POST.get('lastName') != "":
            if check_box:        
                genderSet = {"male":0, "female":1}
                # stu = Student.objects.get(stu_id=userID)
                # if request.POST.get('firstName') != "":
                #     stu.stu_fname = request.POST.get('firstName')
                # if request.POST.get('lastName') != "":    
                #     stu.stu_lname = request.POST.get('lastName')
                if request.POST.get('phoneNum') != "":    
                    stu.stu_phone = request.POST.get('phoneNum')
                if request.POST.get('university') != "":     
                    stu.stu_c_uni = request.POST.get('university')
                if request.POST.get('major') != "": 
                    stu.stu_major = request.POST.get('major')

                if request.POST.get('gender') != "":
                    gender = str(request.POST.get('gender'))
                    gender = gender.lower()
                    if genderSet.__contains__(gender) == True:
                        stu.stu_gender = genderSet.get(gender)
            stu.save()
            return redirect('/stu/profile/%s' %userID)
        else:
            message = "First name and last name should be filled!" 
        return render(request, 'stu/personal-edit.html', {"message": message}) 
    return render(request, 'stu/personal-edit.html')
