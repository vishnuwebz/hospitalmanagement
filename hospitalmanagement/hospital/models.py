from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone
from django.contrib.auth.hashers import make_password


# Create your models here.

class Department(models.Model):
    # objects = None
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name


# class Doctors(models.Model):
#     #
#
#     #
#     doc_name = models.CharField(max_length=255)
#     doc_spec = models.CharField(max_length=255)
#     dep_name = models.ForeignKey(Department, on_delete=models.CASCADE)
#     doc_image = models.ImageField(upload_to='doctors')
#     def __str__(self):
#         return self.doc_name


# from django.db import models
#
# class Department(models.Model):
#     dep_name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.dep_name

# class Doctor(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     contact = models.CharField(max_length=15)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     doc_spec = models.CharField(max_length=255)
#     availability = models.CharField(max_length=10)
#     doc_image = models.ImageField(upload_to='doctors/', null=True, blank=True)
#     date_joined = models.DateField(auto_now_add=True)
#     new_department_name = models.CharField(max_length=100, blank=True)
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"


######### from dash board app #########
class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('admin_panel', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, default='patient')


# class Patient(models.Model):
#     first_name = models.CharField(max_length=50, default='')
#     last_name = models.CharField(max_length=50, default='')
#     email = models.EmailField(unique=True, default='')
#     contact = models.CharField(max_length=15)
#     password = models.CharField(max_length=128, default='')
#
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#
#
#     date_of_birth = models.DateField(default=timezone.now)
#     address = models.TextField(default='')
#     gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
#                               default='Male')
#     medical_history = models.TextField(blank=True)
#     date_created = models.DateTimeField(default=timezone.now)
#     date_updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"




# class Patient(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)
#     contact = models.CharField(max_length=15)
#     password = models.CharField(max_length=128)
#     date_of_birth = models.DateField()
#     address = models.TextField()
#     GENDER_CHOICES = [
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#         ('Other', 'Other'),
#     ]
#     gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
#     medical_history = models.TextField(blank=True)
#     date_created = models.DateTimeField(default=timezone.now)
#     date_updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    email = models.EmailField(unique=True, default='')
    contact = models.CharField(max_length=15)
    date_of_birth = models.DateField(default=timezone.now)
    address = models.TextField(default='')
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male')
    medical_history = models.TextField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# class Doctor(models.Model):
#     DEPARTMENT_CHOICES = [
#         ('Cardiology', 'Cardiology'),
#         ('Neurology', 'Neurology'),
#         ('Pediatrics', 'Pediatrics'),
#         ('Orthopedics', 'Orthopedics'),
#         ('General', 'General'),
#     ]
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=50, default='')
#     last_name = models.CharField(max_length=50, default='')
#     email = models.EmailField(unique=True, default='')
#     contact = models.CharField(max_length=15, default='')
#     department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, default='General')
#     availability = models.CharField(max_length=50, default='Unknown')
#     date_joined = models.DateField(auto_now_add=True)
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f"Dr. {self.first_name} {self.last_name} - ({self.department})"
#


# class Doctor(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)
#     contact = models.CharField(max_length=15)
#     department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
#     new_department_name = models.CharField(max_length=100, blank=True)
#     doc_spec = models.CharField(max_length=255)
#     availability = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')], default='')
#     date_joined = models.DateField(auto_now_add=True)
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#     doc_image = models.ImageField(upload_to='doctors', blank=True, null=True)
#
#     def __str__(self):
#         return f"Dr. {self.first_name} {self.last_name} - ({self.department or self.new_department_name})"


# latest
# class Doctor(models.Model):
#
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     contact = models.CharField(max_length=15)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     # new_department_name = models.CharField(max_length=100, blank=True)
#
#     doc_spec = models.CharField(max_length=255)
#     availability = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes')
#     doc_image = models.ImageField(upload_to='doctors', blank=True, null=True)
#     date_joined = models.DateField(auto_now_add=True)
#
#     # class Meta:
#     #     # This will tell Django to create and manage the database table for this model
#     #     managed = True
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name} - ({self.department.name})"
#
#     class Meta:
#         verbose_name = "Doctor"
#         verbose_name_plural = "Doctors"


class Doctor(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor')

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doc_spec = models.CharField(max_length=255)
    availability = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes')
    doc_image = models.ImageField(upload_to='doctors', blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - ({self.department.dep_name})"

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"


class Admin(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username


class DoctorProfile(models.Model):
    doctor = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=255)

    def __str__(self):
        return f"Dr. {self.user.get_full_name()} ({self.department})"


# class Appointment(models.Model):
#     patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments_as_patient")
#     doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments_as_doctor")
#     doctor_department = models.CharField(max_length=255, default='General')
#     date = models.DateField()
#     time = models.TimeField()
#     symptoms = models.TextField(blank=True, null=True)
#
#     def __str__(self):
#         return f"{self.patient.username} with {self.doctor.username} - ({self.doctor_department}) on {self.date} at {self.time}"


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments_as_patient")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments_as_doctor")
    date = models.DateField()
    time = models.TimeField()
    symptoms = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient.first_name} {self.patient.last_name} with Dr. {self.doctor.first_name} {self.doctor.last_name} on {self.date} at {self.time}"


class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    status = models.CharField(max_length=50, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')])
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Billing for {self.patient} by {self.doctor}"




class Discharge(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    discharge_date = models.DateField(default=timezone.now)
    discharge_reason = models.TextField()
    discharge_note = models.TextField()

    def __str__(self):
        return f"Discharge of {self.patient} by {self.doctor}"