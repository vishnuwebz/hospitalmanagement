# hospital/admin_urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.panel_index, name="panel_index"),
    # path("patients/", views.admin_patient_list, name='admin_patient_list'),
    # path('admin_panel/patients/', views.admin_patient_list, name='admin_patient_list'),
    path("patients/add/", views.admin_add_patient, name='admin_add_patient'),
    path("patients/edit/<int:pk>/", views.admin_edit_patient, name="admin_edit_patient"),
    path("doctors/", views.admin_doctor_list, name='admin_doctor_list'),
    path("doctors/add/", views.admin_add_doctor, name='admin_add_doctor'),
    path("doctors/edit/<int:pk>/", views.admin_edit_doctor, name="admin_edit_doctor"),
    path("billings/", views.admin_billing_list, name="admin_billing_list"),
    path("billings/add/", views.admin_add_billing, name="admin_add_billing"),
    path("billings/edit/<int:pk>/", views.admin_edit_billing, name="admin_edit_billing"),
    # path('patient/book_appointment/', views.book_appointment, name='book_appointment'),

    # Admin panel views
    path("admin_panel/", views.admin_dashboard, name="admin_dashboard"),
    path('admin_panel/patients/', views.admin_patient_list, name='admin_patient_list'),
    path('admin_panel/patients/add/', views.admin_add_patient, name='admin_add_patient'),
    path('admin_panel/patients/edit/<int:pk>/', views.admin_edit_patient, name="admin_edit_patient"),
    path("admin_panel/doctors/", views.admin_doctor_list, name='admin_doctor_list'),
    path("admin_panel/doctors/add/", views.admin_add_doctor, name='admin_add_doctor'),
    path('admin_panel/doctors/edit/<int:pk>/', views.admin_edit_doctor, name="admin_edit_doctor"),
    path('admin_panel/billings/', views.admin_billing_list, name="admin_billing_list"),
    path("admin_panel/billings/add", views.admin_add_billing, name="admin_add_billing"),
    path("admin_panel/billings/edit/<int:pk>/", views.admin_edit_billing, name="admin_edit_billing"),

    # Admin signup URL pattern
    path('register/admin_panel/', views.admin_register, name='admin_register'),
    path('login/admin_panel/', views.admin_login, name='admin_login'),
    path('admin_signup/', views.admin_signup, name='admin_signup'),

    path('logout/confirmation/', views.logout_confirmation, name='logout_confirmation'),

    # path('admin_panel/billings/edit/<int:pk>/', views.admin_edit_billing, name='admin_edit_billing'),
    # for admin#
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    # path('doctors/', views.admin_doctor_list, name='admin_doctor_list'),
    path('edit_doctor/<int:doctor_id>/', views.admin_edit_doctor, name='admin_edit_doctor'),

    path('patients/edit/<int:pk>/', views.admin_edit_patient, name='admin_edit_patient'),
    path('patients/delete/<int:pk>/', views.admin_delete_patient, name='admin_delete_patient'),
    path('departments/delete/<int:pk>/', views.admin_delete_department, name='admin_delete_department'),
]
