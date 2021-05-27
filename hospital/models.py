from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]

class Contact(models.Model):
    id=models.AutoField(primary_key=True)   
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=12)
    email=models.CharField(max_length=100)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True , blank=True)
    @property
    def __str__(self):
        return "{}".format(self.name) 

class Assdoc_to_Doctor_Messages(models.Model):
    id=models.AutoField(primary_key=True)   
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    assdoctorId=models.PositiveIntegerField(null=True)
    lab_report= models.ImageField(upload_to='Lab_reports/',null=True,blank=True)
    assdoc_name=models.CharField(max_length=255)
    doc_name=models.CharField(max_length=255)
    Patient_name=models.CharField(max_length=255)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True , blank=True)
    #def _str_(self):
    #    return self.doc_name



class doc_to_Assdoc_Messages(models.Model):
    id=models.AutoField(primary_key=True)   
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    assdoctorId=models.PositiveIntegerField(null=True)
    lab_report= models.ImageField(upload_to='Lab_reports/',null=True,blank=True)
    assdoc_name=models.CharField(max_length=255)
    doc_name=models.CharField(max_length=255)
    Patient_name=models.CharField(max_length=255)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True , blank=True)
   # def _str_(self):
     #   return self.assdoc_name



class admitrequest(models.Model):  
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=12)
    assignedassDoctorId = models.PositiveIntegerField(null=True)
    patientId=models.PositiveIntegerField(null=True)
    timestamp=models.DateTimeField(auto_now_add=True , blank=True)
    def _str_(self):
        return self.name

class dischargerequest(models.Model):  
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=12)
    doctor_bill=models.CharField(max_length=12)
    timestamp=models.DateTimeField(auto_now_add=True , blank=True)
    def _str_(self):
        return self.name


class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)

class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    symptoms = models.CharField(max_length=100,null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    assignedassDoctorId = models.PositiveIntegerField(null=True)
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    admit=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name+" ("+self.symptoms+")"


class assDoctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/AssDoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)

class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)
    #@property
    #def __str__(self):
      #  return "{}".format(self.patientName)


class PatientDischargeDetails(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40)
    assignedDoctorName=models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    symptoms = models.CharField(max_length=100,null=True)

    admitDate=models.DateField(null=False)
    releaseDate=models.DateField(null=False)
    daySpent=models.PositiveIntegerField(null=False)

    roomCharge=models.PositiveIntegerField(null=False)
    medicineCost=models.PositiveIntegerField(null=False)
    doctorFee=models.PositiveIntegerField(null=False)
    OtherCharge=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)        