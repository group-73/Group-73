from django import forms
from django.contrib.auth.models import User
from . import models
from hospital.models import admitrequest
from hospital.models import dischargerequest

class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class AdmitrequestForm(forms.ModelForm):
    class Meta:
        model=admitrequest
        fields=['name','phone']
        widgets = {

            'name' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'phone' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            
           
        }

class DischargerequestForm(forms.ModelForm):
    class Meta:
        model=dischargerequest
        fields=['name','phone','doctor_bill']
        widgets = {

            'name' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'phone' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'doctor_bill' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            
           
        }        
       

class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class DoctorForm(forms.ModelForm):
    class Meta:
        model=models.Doctor
        fields=['address','mobile','department','status','profile_pic']



class assDoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        
class assDoctorForm(forms.ModelForm):
    class Meta:
        model=models.assDoctor
        fields=['address','mobile','department','status','profile_pic']

        

class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class PatientForm(forms.ModelForm):
    #this is the extrafield for linking patient and their assigend doctor
    #this will show dropdown __str__ method doctor model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
    assignedDoctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Patient
        fields=['address','mobile','status','symptoms','profile_pic']

class AppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    patientId=forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),empty_label="Patient Name and Symptoms", to_field_name="user_id")
    class Meta:
        model=models.Appointment
        fields=['description','status']


class PatientAppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Appointment
        fields=['description','status']

        
class AssistanttodoctormessageForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    patientId=forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),empty_label="Patient Name and Symptoms", to_field_name="user_id")
    class Meta:
        model=models.Assdoc_to_Doctor_Messages
        fields=['content','lab_report']

class DoctortoassistantmessageForm(forms.ModelForm):
    assdoctorId=forms.ModelChoiceField(queryset=models.assDoctor.objects.all().filter(status=True),empty_label="Assistant Doctor Name", to_field_name="user_id")
    patientId=forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),empty_label="Patient Name and Symptoms", to_field_name="user_id")
    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True), to_field_name="user_id")
    class Meta:
        model=models.doc_to_Assdoc_Messages
        fields=['content','lab_report']


