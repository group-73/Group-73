
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . import forms,models
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test


# Create your views here.


def index(request):
    return render(request, 'index.html')

def adminclick_view(request):
    return render(request, 'adminclick.html')

def patientclick_view(request):
    return render(request, 'patientclick.html')

def doctorclick_view(request):
    return render(request, 'doctorclick.html')

def assdoctorclick_view(request):
    return render(request, 'assdoctorclick.html')


#to save details of admin signup in forms
def adminsignup_view(request):
    form=forms.AdminSigupForm()
    if request.method=='POST':
        form=forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect('adminlogin')
    return render(request,'adminsignup.html',{'form':form})

def doctorsignup_view(request):
    userForm=forms.DoctorUserForm()
    doctorForm=forms.DoctorForm()
    mydict={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorUserForm(request.POST)
        doctorForm=forms.DoctorForm(request.POST,request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            doctor=doctorForm.save(commit=False)
            doctor.user=user
            doctor=doctor.save()
            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)
        return HttpResponseRedirect('doctorlogin')
    return render(request,'doctorsignup.html',context=mydict)

def assdoctorsignup_view(request):
    userForm=forms.assDoctorUserForm()
    doctorForm=forms.assDoctorForm()
    mydict={'userForm':userForm,'assDoctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.assDoctorUserForm(request.POST)
        doctorForm=forms.assDoctorForm(request.POST,request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            doctor=doctorForm.save(commit=False)
            doctor.user=user
            doctor=doctor.save()
            my_adoctor_group = Group.objects.get_or_create(name='ASSDOCTOR')
            my_adoctor_group[0].user_set.add(user)
        return HttpResponseRedirect('assdoctorlogin')
    return render(request,'assdoctorsignup.html',context=mydict)


def patientsignup_view(request):
    userForm=forms.PatientUserForm()
    patientForm=forms.PatientForm()
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST)
        patientForm=forms.PatientForm(request.POST,request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patient=patientForm.save(commit=False)
            patient.user=user
            patient.assignedDoctorId=request.POST.get('assignedDoctorId')
            patient=patient.save()
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
        return HttpResponseRedirect('patientlogin')
    return render(request,'patientsignup.html',context=mydict)


def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()
def is_assDoctor(user):
    return user.groups.filter(name='ASSDOCTOR').exists()

def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('admin-dashboard')
    elif is_doctor(request.user):
        return redirect('doctor-dashboard')
    elif is_patient(request.user):
        return redirect('patient-dashboard')
    elif is_assDoctor(request.user):
        return redirect ('assdoctor-dashboard')
# Create your views here.

#admin all views
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_dashboard_view(request):
     return render(request,'admin_dashboard.html')#context=mydict)

#doctor related all views
@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_dashboard_view(request):
    return render(request,'doctor_dashboard.html')#,conetxt=mydict)

#ass doctor related all views
@login_required(login_url='assdoctorlogin')
@user_passes_test(is_assDoctor)
def assdoctor_dashboard_view(request):
    return render(request,'assdoctor_dashboard.html')#,conetxt=mydict)

#patient related all views

@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_dashboard_view(request):
    return render(request,'patient_dashboard.html')#,conetxt=mydict)