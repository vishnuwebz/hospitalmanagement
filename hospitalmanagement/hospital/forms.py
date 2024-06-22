from django import forms
from django.contrib.auth.models import User
from . import models
from .models import DoctorProfile, Appointment, Department, Doctor


#for admin_panel signup
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }



from .models import Billing

class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['patient', 'doctor', 'amount', 'date', 'status', 'description']



class BookAppointmentForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(queryset=DoctorProfile.objects.all(), label='Doctor')
    appointment_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Appointment Date')
    appointment_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label='Appointment Time')
    symptoms = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), required=False, label='Symptoms')

    class Meta:
        model = Appointment
        fields = ['doctor', 'appointment_date', 'appointment_time', 'symptoms']




# class DepartmentForm(forms.ModelForm):
#     class Meta:
#         model = Department
#         fields = ['dep_name', 'dep_description']


#
# class DoctorForm(forms.ModelForm):
#     class Meta:
#         model = Doctor
#         fields = ['first_name', 'last_name', 'email', 'contact', 'department', 'doc_spec', 'availability', 'doc_image']
#         widgets = {
#             'department': forms.Select()
#         }
#
# class DoctorRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Doctor
#         fields = [
#             'user', 'first_name', 'last_name', 'email', 'contact', 'department',
#             'doc_spec', 'availability', 'doc_image'
#         ]
#
#
# #for doctor related form
# class DoctorUserForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['first_name','last_name','username','password']
#         widgets = {
#         'password': forms.PasswordInput()
#         }
# class DoctorForm(forms.ModelForm):
#     class Meta:
#         model=models.Doctor
#         fields=['address','mobile','department','status','profile_pic']
#
#
#
# #for patient related form
# class PatientUserForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['first_name','last_name','username','password']
#         widgets = {
#         'password': forms.PasswordInput()
#         }
# class PatientForm(forms.ModelForm):
#     #this is the extrafield for linking patient and their assigend doctor
#     #this will show dropdown __str__ method doctor model is shown on html so override it
#     #to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
#     assignedDoctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")
#     class Meta:
#         model=models.Patient
#         fields=['address','mobile','status','symptoms','profile_pic']
#
#
#
# class AppointmentForm(forms.ModelForm):
#     doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
#     patientId=forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),empty_label="Patient Name and Symptoms", to_field_name="user_id")
#     class Meta:
#         model=models.Appointment
#         fields=['description','status']
#
#
# class PatientAppointmentForm(forms.ModelForm):
#     doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
#     class Meta:
#         model=models.Appointment
#         fields=['description','status']
#
#
# #for contact us page
# class ContactusForm(forms.Form):
#     Name = forms.CharField(max_length=30)
#     Email = forms.EmailField()
#     Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
#
#
#



from django import forms
from .models import Doctor, Department

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [
            'first_name', 'last_name', 'email', 'contact',
            'department', 'doc_spec', 'availability', 'doc_image'
        ]

# class DepartmentForm(forms.ModelForm):
#     class Meta:
#         model = Department
#         fields = ['dep_name', 'dep_description']
