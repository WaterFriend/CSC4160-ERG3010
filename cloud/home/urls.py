from django.urls import path

from . import views
#from .views import SearchResultsView

urlpatterns = [
    path('<str:userID>', views.result_list, name = 'result_list'),
    #path('search/', SearchResultsView.as_view(), name='search_result'),
]