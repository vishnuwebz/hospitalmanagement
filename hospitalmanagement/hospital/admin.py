from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Department) #new
# admin.site.register(Doctors)

print("Registering Doctor model...")
from .models import Doctor
admin.site.register(Doctor)
print("Doctor model registered successfully.")

#new

admin.site.register(Patient)
# admin.site.register(Doctor)
admin.site.register(Billing)
admin.site.register(Appointment)

# admin_panel.site.register(Profile)
admin.site.register(Admin)
admin.site.register(DoctorProfile)
admin.site.register(Discharge)
# admin_panel.site.register(CustomUser)
