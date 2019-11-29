from django.shortcuts               import render, redirect
from django.views.generic           import TemplateView, FormView, ListView
from django.core.files.storage      import FileSystemStorage
from django.contrib.staticfiles     import finders
from django.db.models               import Q
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf   import csrf_exempt



@csrf_exempt
def result_list(request, doctorID):
    content = []
    return render(request, 'base.html', content)      
