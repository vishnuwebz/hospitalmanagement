from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[


    ### doctor ###
    path('doctor/register/', views.doctor_register, name='doctor_register'),
    path('doctor/login/', views.doctor_login, name='doctor_login'),
    path('doctor/logout/confirmation/', views.doctor_logout_confirmation, name='doctor_logout_confirmation'),
    path('doctor/add/', views.add_doctor, name='add_doctor'),
    path("dashboard/doctor/", views.doctor_dashboard, name="doctor_dashboard"),

    # path('logout/', views.logout_view, name='logout'),





# CRUD operations
    path('patients/', views.patient_list, name='patient_list'),
    # path('patient/book_appointment/', views.book_appointment, name='book_appointment'),
    path('patients/add/', views.add_patient, name="add_patient"),
    path('patients/edit/<int:pk>/', views.edit_patient, name="edit_patient"),
    # path('doctors/', views.doctor_list, name="doctor_list"),
    # path("doctors/add/", views.add_doctor, name="add_doctor"),
    path('doctor/edit/<int:pk>/', views.doctor_edit_doctor, name='doctor_edit_doctor'),
    path('admin/doctor/<int:doctor_id>/delete/', views.admin_delete_doctor, name='admin_delete_doctor'),
    path("billings/", views.billing_list, name="billing_list"),
    path("billings/add/", views.add_billing, name="add_billing"),
    path('billings/edit/<int:billing_id>/', views.edit_billing, name='edit_billing'),
    path("doctor_patient_bill/", views.doctor_patient_bill, name="doctor_patient_bill"),
    path("report/", views.report, name='report'),



    path('patient/<int:patient_id>/discharge/', views.discharge_patient, name='discharge_patient'),
    path('discharge/', views.discharge_list, name='discharge_list'),
    path('discharge/<int:discharge_id>/', views.discharge_detail, name='discharge_detail'),

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
#

]