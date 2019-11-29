from django.urls import path

from . import views

urlpatterns = [
    path('<str:doctorID>', views.upload, name='upload'),
]