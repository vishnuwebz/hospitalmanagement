from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[

    ### patient ###
    path('register/patient/', views.patient_register, name='patient_register'),
    path('login/patient/', views.patient_login, name='patient_login'),
    path("dashboard/patient/", views.patient_dashboard, name="patient_dashboard"),

    path('logout/', views.logout_view, name='logout'),
    path('logout/confirmation/', views.patient_logout_confirmation, name='patient_logout_confirmation'),

    path("bill/patient/", views.patient_bill_view, name="patient_bill_view"),

    path("view/departments/", views.patient_view_department, name="patient_view_department"),

    path("patient_view_doctors/", views.patient_view_doctors, name="patient_view_doctors"),



    path("patient_book_appointment/", views.patient_book_appointment, name='patient_book_appointment'),

    path("patient/appointments", views.patient_appointment_list, name="patient_appointment_list"),

    path('delete-appointment/<int:pk>/', views.patient_delete_appointment, name='patient_delete_appointment'),

    path('edit-appointment/<int:pk>/', views.patient_edit_appointment, name='patient_edit_appointment'),



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


]