from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('meetme/<slug:meetme_slug>/success', views.confirm_registration, name='confirm-registration'),
    path('meetme/<slug:meetme_slug>', views.meetme_details, name='meetme_details'), 
    
]

