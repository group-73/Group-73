from django.contrib import admin
from .models import Doctor,Patient,assDoctor,Contact,Appointment,PatientDischargeDetails,admitrequest,dischargerequest,Assdoc_to_Doctor_Messages,doc_to_Assdoc_Messages,Patient_Bill_Messages
# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(assDoctor)
admin.site.register(Appointment)
admin.site.register(Contact)
admin.site.register(PatientDischargeDetails)
admin.site.register(admitrequest)
admin.site.register(dischargerequest)
admin.site.register(Assdoc_to_Doctor_Messages)
admin.site.register(doc_to_Assdoc_Messages)
admin.site.register(Patient_Bill_Messages)
