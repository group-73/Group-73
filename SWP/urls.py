"""SWP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from hospital import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
  #  path('', include('hospital.urls')),
  path('', views.index,name='index'),
    path('adminclick/',views.adminclick_view,name='adminclick'),
    path('patientclick',views.patientclick_view,name='patientclick'),
    path('doctorclick',views.doctorclick_view,name='doctorclick'),
    path('assdoctorclick',views.assdoctorclick_view,name='assdoctorclick'),

    #admin sginup and login
    path('adminsignup',views.adminsignup_view, name='adminsignup'),
    path('adminlogin',LoginView.as_view(template_name='hospital/adminl.html')),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    #patient signup and login
    path('patientsignup',views.patientsignup_view, name='patientsignup'),
    path('patientlogin',LoginView.as_view(template_name='patientlogin.html')),
    path('patient-dashboard', views.patient_dashboard_view,name='patient-dashboard'),


    #doctor signup and login
    path('doctorsignup',views.doctorsignup_view, name='doctorsignup'),
    path('doctorlogin',LoginView.as_view(template_name='doctorlogin.html')),
    path('doctor-dashboard', views.doctor_dashboard_view,name='doctor-dashboard'),

    #assdoctor signup and login
     path('assdoctorsignup',views.assdoctorsignup_view, name='assdoctorsignup'),
    path('assdoctorlogin',LoginView.as_view(template_name='assdoctorlogin.html')),
    path('assdoctor-dashboard', views.assdoctor_dashboard_view,name='assdoctor-dashboard'),



    path('afterlogin', views.afterlogin_view,name='afterlogin')
 
    
]
