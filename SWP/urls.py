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
    path('adminclickk',views.adminclick_view,name='adminclick'),
    path('patientclick',views.patientclick_view,name='patientclick'),
    path('doctorclick',views.doctorclick_view,name='doctorclick'),
    path('assdoctorclick',views.assdoctorclick_view,name='assdoctorclick'),


    #Messages
    path('assdoc-to-doctor-messages',views.assdoc_to_doctor_messages_view, name='assdoc_to_doctor_messages'),
    path('assdoc-to-doctor',views.assdoc_to_doctor_view, name='assdoc_to_doctor'),
    path('doc-to-assdoc-messages',views.doc_to_assdoc_messages_view, name='doc_to_assdoc_messages'),
    path('doc-to-assdoc',views.doc_to_assdoc_view, name='doc_to_assdoc'),
    
    path('patient-bill-message',views.patient_bill_message_view, name='patient-bill-message'),
    path('admin-patient-bill-message',views.admin_patient_bill_message_view, name='admin-patient-bill-message'),


    #admin sginup and login
    path('adminsignup',views.adminsignup_view, name='adminsignup'),
    path('adminlogin',LoginView.as_view(template_name='hospital/adminl.html')),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    path('admin-messages',views.admin_messages_view, name='admin-messages'),
    path('Contactdelete', views.Contactdelete, name='Contactdelete'),

    #patient signup and login
    path('patientsignup',views.patientsignup_view, name='patientsignup'),
    path('patientlogin',LoginView.as_view(template_name='patientlogin.html')),
    #patient dashboard left side views
    path('patient-dashboard', views.patient_dashboard_view,name='patient-dashboard'),
    path('patient-appointment', views.patient_appointment_view,name='patient-appointment'),
    path('patient-book-appointment', views.patient_book_appointment_view,name='patient-book-appointment'),
    path('patient-view-appointment', views.patient_view_appointment_view,name='patient-view-appointment'),
    path('patient-discharge', views.patient_discharge_view,name='patient-discharge'),


    #doctor signup and login
    path('doctorsignup',views.doctorsignup_view, name='doctorsignup'),
    path('doctorlogin',LoginView.as_view(template_name='doctorlogin.html')),
    path('doctor-dashboard', views.doctor_dashboard_view,name='doctor-dashboard'),
    path('admit_request_from_doctor',views.admit_request_from_doctor,name='admit_request_from_doctor'),
    path('discharge_request_from_doctor',views.discharge_request_from_doctor,name='discharge_request_from_doctor'),


    #doctor dashboard left side all views
    path('doctor-patient', views.doctor_patient_view,name='doctor-patient'),
    path('doctor-appointment', views.doctor_appointment_view,name='doctor-appointment'),
    path('doctor-view-appointment', views.doctor_view_appointment_view,name='doctor-view-appointment'),
    path('doctor-delete-appointment',views.doctor_delete_appointment_view,name='doctor-delete-appointment'),
    path('doctor-view-patient', views.doctor_view_patient_view,name='doctor-view-patient'),
    path('doctor-view-discharge-patient',views.doctor_view_discharge_patient_view,name='doctor-view-discharge-patient'),
    path('delete-appointment/<int:pk>', views.delete_appointment_view,name='delete-appointment'),
    path('assdoctor-message-delete', views.assdoctor_message_delete_view, name='assdoctor-message-delete'),
    

    #assdoctor signup and login
    path('assdoctorsignup',views.assdoctorsignup_view, name='assdoctorsignup'),
    path('assdoctorlogin',LoginView.as_view(template_name='assdoctorlogin.html')),
    path('assdoctor-dashboard', views.assdoctor_dashboard_view,name='assdoctor-dashboard'),
    path('assdoctor-patient', views.assdoctor_patient_view,name='assdoctor-patient'),
    path('doctor-message-delete', views.doctor_message_delete_view, name='doctor-message-delete'),
    path('assdoctor-view-patient', views.assdoctor_view_patient_view,name='assdoctor-view-patient'),
    path('admin-approve-assdoctor', views.admin_approve_assdoctor_view,name='admin-approve-assdoctor'),
    path('approve-assdoctor/<int:pk>', views.approve_assdoctor_view,name='approve-assdoctor'),
    path('reject-assdoctor/<int:pk>', views.reject_assdoctor_view,name='reject-assdoctor'),



    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='index.html'),name='logout'),

    path('admin-doctor', views.admin_doctor_view,name='admin-doctor'),
    path('admin-approve-doctor', views.admin_approve_doctor_view,name='admin-approve-doctor'),
    path('delete-doctor-from-hospital/<int:pk>', views.delete_doctor_from_hospital_view,name='delete-doctor-from-hospital'),
    path('update-doctor/<int:pk>', views.update_doctor_view,name='update-doctor'),
    path('admin-add-doctor', views.admin_add_doctor_view,name='admin-add-doctor'),
    path('approve-doctor/<int:pk>', views.approve_doctor_view,name='approve-doctor'),
    path('reject-doctor/<int:pk>', views.reject_doctor_view,name='reject-doctor'),
    path('admin-view-doctor', views.admin_view_doctor_view,name='admin-view-doctor'),
    path('admin-view-doctor-specialisation',views.admin_view_doctor_specialisation_view,name='admin-view-doctor-specialisation'),

    path('admin-patient', views.admin_patient_view,name='admin-patient'),
    path('admin-view-patient', views.admin_view_patient_view,name='admin-view-patient'),
    path('delete-patient-from-hospital/<int:pk>', views.delete_patient_from_hospital_view,name='delete-patient-from-hospital'),
    path('update-patient/<int:pk>', views.update_patient_view,name='update-patient'),
    path('admin-add-patient', views.admin_add_patient_view,name='admin-add-patient'),
    path('admin-approve-patient', views.admin_approve_patient_view,name='admin-approve-patient'),
    path('approve-patient/<int:pk>', views.approve_patient_view,name='approve-patient'),
    path('admin-discharge-patient', views.admin_discharge_patient_view,name='admin-discharge-patient'), 
    path('discharge-patient/<int:pk>', views.discharge_patient_view,name='discharge-patient'),
    path('download-pdf/<int:pk>', views.download_pdf_view,name='download-pdf'),
    path('reject-patient/<int:pk>', views.reject_patient_view,name='reject-patient'),
    path('admitpatient',views.admit_patient,name='admitpatient'),
    path('dischargepatient',views.dischargepatient,name='dischargepatient'),
    path('admin-appointment', views.admin_appointment_view,name='admin-appointment'),
    path('admin-view-appointment', views.admin_view_appointment_view,name='admin-view-appointment'),
    path('admin-add-appointment', views.admin_add_appointment_view,name='admin-add-appointment'),
    path('admin-approve-appointment', views.admin_approve_appointment_view,name='admin-approve-appointment'),
    path('approve-appointment/<int:pk>', views.approve_appointment_view,name='approve-appointment'),
    path('reject-appointment/<int:pk>', views.reject_appointment_view,name='reject-appointment'),
    path('requestadmitdelete',views.request_admit_delete_view,name='requestadmitdelete'),
    path('dischargerequestadmitdelete',views.dischargerequestadmitdelete,name='dischargerequestadmitdelete'),
    
   # path('image-display/<int:pk>',views.image_display_view,name='image-display')
 
    
    
]
