from django.shortcuts               import render, redirect, render_to_response
from django.views.generic           import TemplateView, FormView, ListView
from django.core.files.storage      import FileSystemStorage
from django.contrib.staticfiles     import finders
from django.contrib.auth            import logout
from django.contrib                 import messages
from django.contrib.auth.decorators import login_required
from django.db.models               import Q
from django.views.decorators.csrf   import csrf_exempt

# Create your views here.
from upload.models                  import Patient

@csrf_exempt
def result(request, doctorID, patientID):
    if request.method == "GET":
        patient     = Patient.objects.get(pID = patientID)
        firstName   = patient.pFName
        lastName    = patient.pLName
        gender      = patient.pGender
        race        = patient.pRace
        ethnicity   = patient.pEthnicity
        status      = patient.pStatus
        remark      = patient.pRemark
        age         = patient.pAge

        content = {
            'firstName' : firstName,
            'lastName'  : lastName,
            'gender'    : gender,
            'race'      : race,
            'ethnicity' : ethnicity,
            'status'    : status,
            'remark'    : remark,
            'age'       : age,
            "backLink"  : "../../home/" + doctorID,
        }

        return render(request, 'detailed_preview.html', content)  #TODO
        
    elif request.method == "POST":   
        logout(request) 
        return redirect('../login/login')