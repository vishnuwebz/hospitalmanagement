from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('', views.homebase, name='homebase'),
    path('home', views.home, name='home'),
    path('aboutus', views.aboutus, name='aboutus'),#name is use to swith btw html using this key name valu(html) will be returned
    path('contact', views.contact, name='contact'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
    path('departments', views.departments, name='departments'),
    path('doctors', views.doctors, name='doctors'),
    path('services',views.services, name='services'),
    path('book/', views.book, name='book'),


    path('admin_panel/billings/edit/<int:pk>/', views.admin_edit_billing, name='admin_edit_billing'),
    #for admin#
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('doctors/', views.admin_doctor_list, name='admin_doctor_list'),
    path('edit_doctor/<int:doctor_id>/', views.admin_edit_doctor, name='admin_edit_doctor'),


#     ###  from dashboard app ####
# # Dashboard related views
    path('dashboard_home/', views.dashboard_home, name='dashboard_home'),



    path('departments/', views.department_list, name='department_list'),
    path('departments/add/', views.add_department, name='add_department'),

    path('departments/edit/<int:pk>/', views.edit_department, name='edit_department'),


#     # path('adminsignup/', views.adminsignup, name='adminsignup'),
#     # path('adminlogin/', views.adminlogin, name='adminlogin'),
#     # path('doctorsignup/', views.doctorsignup, name='doctorsignup'),
#     # path('doctorlogin/', views.doctorlogin, name='doctorlogin'),
#     # path('patientsignup/', views.patientsignup, name='patientsignup'),
#     # path('patientlogin/', views.patientlogin, name='patientlogin'),
#     # path('patientindex/', views.patientindex, name='patientindex'),
#
#     path('admin_signup/', views.admin_signup_view, name='admin_signup'),
#     # path('admin_login/', LoginView.as_view(template_name='dashboard/admin_login.html'), name='admin_login'),
#
#     ### patient ###
#     path('register/patient/', views.patient_register, name='patient_register'),
#     path('login/patient/', views.patient_login, name='patient_login'),
#     path("dashboard/patient/", views.patient_dashboard, name="patient_dashboard"),
#
#     ### doctor ###
#     path('register/doctor/', views.doctor_register, name='doctor_register'),
#     path('login/doctor/', views.doctor_login, name='doctor_login'),
#     path("dashboard/doctor/", views.doctor_dashboard, name="doctor_dashboard"),
#
#     ### admin_panel ###
#     path('register/admin_panel/', views.admin_register, name='admin_register'),
#     path('login/admin_panel/', views.admin_login, name='admin_login'),
#     path("dashboard/admin_panel/", views.admin_dashboard, name="admin_dashboard"),
#
#
# # Logout view
#     # path('register/', views.register, name='register'),
#     # path('login/', views.login_view, name="login"),
#     # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
#     path('logout/', views.logout_view, name='logout'),
#
#
#
#
#
# # CRUD operations
#     path('patients/', views.patient_list, name='patient_list'),
#     # path('patient/book_appointment/', views.book_appointment, name='book_appointment'),
#     path('patients/add/', views.add_patient, name="add_patient"),
#     path('patients/edit/<int:pk>/', views.edit_patient, name="edit_patient"),
#     path('doctors/', views.doctor_list, name="doctor_list"),
#     path("doctors/add/", views.add_doctor, name="add_doctor"),
#     path("doctors/edit/<int:pk>/", views.edit_doctor, name="edit_doctor"),
#     path("billings/", views.billing_list, name="billing_list"),
#     path("billings/add/", views.add_billing, name="add_billing"),
#     path("report/", views.report, name='report'),
#
#
# # Admin admin_panel views
#     ####admin_panel####
# #add,edit of patient,doctor,billing
#     path("admin_panel/", views.admin_dashboard, name="admin_dashboard"),
#     path('admin_panel/patients/', views.admin_patient_list, name='admin_patient_list'),
#     path('admin_panel/patients/add/', views.admin_add_patient, name='admin_add_patient'),
#     path('admin_panel/patients/edit/<int:pk>/', views.admin_edit_patient, name="admin_edit_patient"),
#     path("admin_panel/doctors/", views.admin_doctor_list, name='admin_doctor_list'),
#     path("admin_panel/doctors/add/", views.admin_add_doctor, name='admin_add_doctor'),
#     path('admin_panel/doctors/edit/<int:pk>/', views.admin_edit_doctor, name="admin_edit_doctor"),
#     path('admin_panel/billings/', views.admin_billing_list, name="admin_billing_list"),
#     path("admin_panel/billings/add", views.admin_add_billing, name="admin_add_billing"),
#     path("admin_panel/billings/edit/<int:pk>/", views.admin_edit_billing, name="admin_edit_billing"),

# Custom admin admin_panel view
#     path("index/", views.panel_index, name="panel_index"),
]