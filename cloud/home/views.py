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

from upload.models      import Patient


@csrf_exempt
def result_list(request, doctorID):
    if request.method == "GET":
        if '' in request.GET:
            return render(request, 'home.html')
        else:
            patientList = Patient.objects.all()
            content = {
                'uploadLink'  : "../upload/" + doctorID,
                'patient'     : patientList.filter(dID=doctorID)
            }
            return render(request, 'home.html', content)  
    
    
    elif request.method == "POST":
        if 'logout' in request.POST:   
            logout(request) 
            return redirect('../login/login')
        elif '' in request.POST:
            patientID
            return redirect('../result/%s' %doctorID)
