from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect,  HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


from django.db import IntegrityError

from django.db.models import Sum
from django.contrib.auth.models import User
from .models import Doctor

# User = get_user_model()

# Create your views here.
def homebase(request):
    dict_docs0 = {"doctors": Doctor.objects.all()}
    return render(request, "base/homebase.html", dict_docs0)

def book(request):
    return render(request, 'base/book.html')

def home(request):
    return render(request, "base/home.html")


def aboutus(request):
    return render(request, "base/aboutus.html")


def contact(request):
    return render(request, "base/contact.html")

from django.core.mail import send_mail
def contact_submit(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Process the data as needed (e.g., send an email)
        send_mail(
            f"Message from {name}",
            message,
            email,
            ['vishnuwebz@gmail.com'],  # replace with your admin email
            fail_silently=False,
        )
        messages.success(request, 'Thank you for your message. We will get back to you soon.')
        return redirect('contact')

    return redirect('contact')
def departments(request):
    dict_dept = {"dept": Department.objects.all()}
    return render(request, "base/departments.html", dict_dept)




def doctors(request):
    dict_docs = {"doctors": Doctor.objects.all()}
    return render(request, "base/doctors.html", dict_docs)


def services(request):
    return render(request, "base/services.html")


def dashboard_home(request):
    return render(request, "dashboard/dashboard_base.html")

#REGISTER VIEWS
# def patient_register(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         contact = request.POST['contact']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#
#         if password1 == password2:
#             user = User.objects.create(username=email, email=email, first_name=first_name, last_name=last_name, password=make_password(password1))
#             Patient.objects.create(user=user, first_name=first_name, last_name=last_name, email=email, contact=contact)
#             return redirect('patient_login')
#         else:
#             # Passwords don't match, handle this case accordingly
#             return render(request, 'patient/registration_patient.html', {'error': 'Passwords do not match'})
#
#     return render(request, 'patient/registration_patient.html')


def patient_register(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Check if passwords match
        if password1 != password2:
            return render(request, 'patient/registration_patient.html', {'error': 'Passwords do not match'})

        # Check if the email is already registered
        if User.objects.filter(username=email).exists():
            return render(request, 'patient/registration_patient.html', {'error': 'Email is already registered'})

        # Create User and Patient objects
        user = User.objects.create(
            username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=make_password(password1)
        )
        Patient.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            email=email,
            contact=contact
        )

        # Redirect to patient login page after successful registration
        return redirect('patient_login')

    return render(request, 'patient/registration_patient.html')



#LOGIN VIEWS

# def patient_login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user = User.objects.filter(username=email).first()
#         if user and check_password(password, user.password):
#             # Patient authentication successful, redirect to patient dashboard
#             return redirect('patient_dashboard')#patient_dashboard #panel_index
#         else:
#             # Patient authentication failed, provide an error message
#             return render(request, 'patient/login_patient.html', {'error': 'Invalid email or password'})
#
#     return render(request, 'patient/login_patient.html')



from django.contrib.auth import authenticate, login
def patient_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('patient_dashboard')
        else:
            return render(request, 'patient/login_patient.html', {'error': 'Invalid email or password'})

    return render(request, 'patient/login_patient.html', {'error': None})


@login_required
def patient_dashboard(request):
    # Retrieve the Patient instance for the current logged-in user
    patient = get_object_or_404(Patient, user=request.user)

    # Retrieve appointments for the current logged-in patient
    appointments = Appointment.objects.filter(patient=patient)

    context = {
        'user': request.user,
        'appointments': appointments,
    }
    return render(request, 'patient/patient_dashboard.html', context)

@login_required
def patient_view_department(request):
    departments = Department.objects.all()

    context = {
        'dept': departments,
    }
    return render(request, 'patient/patient_view_departments.html', context)

@login_required()
def patient_view_doctors(request):


    dict_docs2 = {"doctors": Doctor.objects.all()}

    return render(request, 'patient/patient_view_doctors.html', dict_docs2)

from .models import Billing, Patient

# @login_required
# def patient_bill_view(request):
#     user = request.user
#     # Fetch the Patient instance associated with the logged-in user
#     try:
#         patient = Patient.objects.get(user=user)
#     except Patient.DoesNotExist:
#         patient = None
#
#     # Fetch the Billing instances associated with this patient
#     if patient:
#         billings = Billing.objects.filter(patient=patient)
#     else:
#         billings = []
#
#     context = {
#         'user': user,
#         'billings': billings,
#     }
#     return render(request, 'patient/patient_bill.html', context)





@login_required
def patient_bill_view(request):
    user = request.user
    try:
        patient = Patient.objects.get(user=user)
    except Patient.DoesNotExist:
        patient = None

    if patient:
        # Fetch all billings for the patient
        billings = Billing.objects.filter(patient=patient)

        # Calculate total amount billed to the patient
        total_amount_patient = billings.aggregate(Sum('amount'))['amount__sum'] or 0
    else:
        billings = []
        total_amount_patient = 0

    # Calculate gross total amount billed across all patients
    gross_total_amount = Billing.objects.aggregate(Sum('amount'))['amount__sum'] or 0

    context = {
        'user': user,
        'billings': billings,
        'total_amount_patient': total_amount_patient,
        'gross_total_amount': gross_total_amount,
    }
    return render(request, 'patient/patient_bill.html', context)

# def doctor_register(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         contact = request.POST['contact']
#         department = request.POST['department']
#         availability = request.POST['availability']
#
#         if password1 == password2:
#             try:
#                 # Check if a user with the provided email already exists
#                 if User.objects.filter(email=email).exists():
#                     raise IntegrityError("Email already exists")
#
#                 # Create a new user
#                 user = User.objects.create_user(username=email, email=email, password=password1,
#                                                 first_name=first_name, last_name=last_name)
#
#                 # Create a new doctor
#                 doctor = Doctor.objects.create(
#                     user=user,
#                     contact=contact,
#                     department=department,
#                     availability=availability
#                 )
#                 return redirect('doctor_login')
#             except IntegrityError as e:
#                 return render(request, 'doctor/registration_doctor.html', {'error': 'Email already exists'})
#         else:
#             return render(request, 'doctor/registration_doctor.html', {'error': 'Passwords do not match'})
#
#     return render(request, 'doctor/registration_doctor.html')


# def doctor_register(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         contact = request.POST['contact']
#         department = request.POST['department']
#         availability = request.POST['availability']
#
#         if password1 == password2:
#             try:
#                 if User.objects.filter(email=email).exists():
#                     raise IntegrityError("Email already exists")
#
#                 user = User.objects.create_user(username=email, email=email, password=password1,
#                                                 first_name=first_name, last_name=last_name)
#
#                 doctor = Doctor.objects.create(
#                     user=user,
#                     first_name=first_name,
#                     last_name=last_name,
#                     email=email,
#                     contact=contact,
#                     department=department,
#                     availability=availability
#                 )
#                 return redirect('doctor_login')
#             except IntegrityError as e:
#                 return render(request, 'doctor/registration_doctor.html', {'error': 'Email already exists'})
#         else:
#             return render(request, 'doctor/registration_doctor.html', {'error': 'Passwords do not match'})
#
#     return render(request, 'doctor/registration_doctor.html', )


# def doctor_register(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         contact = request.POST['contact']
#         department_id = request.POST.get('department')
#         # new_department_name = request.POST.get('new_department_name')
#         availability = request.POST['availability']
#
#         if password1 == password2:
#             try:
#                 if User.objects.filter(email=email).exists():
#                     raise IntegrityError("Email already exists")
#
#                 user = User.objects.create_user(username=email, email=email, password=password1,
#                                                 first_name=first_name, last_name=last_name)
#
#                 if department_id:
#                     department = Department.objects.get(id=department_id)
#                 # elif new_department_name:
#                     #department = Department.objects.create(dep_name=new_department_name)
#                 else:
#                     department = None
#
#                 doctor = Doctor.objects.create(
#                     user=user,
#                     first_name=first_name,
#                     last_name=last_name,
#                     email=email,
#                     contact=contact,
#                     department=department,
#                     availability=availability
#                 )
#                 return redirect('doctor_login')
#             except IntegrityError as e:
#                 return render(request, 'doctor/registration_doctor.html', {'error': 'Email already exists'})
#         else:
#             return render(request, 'doctor/registration_doctor.html', {'error': 'Passwords do not match'})
#
#     return render(request, 'doctor/registration_doctor.html', {'departments': Department.objects.all()})



# def doctor_register(request):
#     departments = Department.objects.all()  # Get all departments for dropdown
#     if request.method == 'POST':
#         #username = request.POST['username']  # Optional username field (not used for login)
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         contact = request.POST['contact']
#         department_id = request.POST['department']
#         doc_spec = request.POST['doc_spec']
#         availability = request.POST['availability']
#         doc_image = request.FILES.get('doc_image')  # Access uploaded image file
#
#         # Validation checks
#         if password1 != password2:
#             messages.error(request, 'Passwords do not match.')
#             return render(request, 'doctor_register.html', {'departments': departments, 'username': username, 'email': email, 'first_name': first_name, 'last_name': last_name})
#
#         # User creation using email
#         user = User.objects.create_user(email, email, password1)  # Email as username
#
#         # Doctor data saving
#         doctor = Doctor.objects.create(
#             user=user,
#             #username=username,  # Optional username field
#             first_name=first_name,
#             last_name=last_name,
#             contact=contact,
#             department_id=department_id,
#             doc_spec=doc_spec,
#             availability=availability,
#             doc_image=doc_image,
#         )
#
#         # Authenticate and login the newly created user
#         user = authenticate(username=email, password=password1)  # Use email for login
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'Doctor registration successful!')
#             return redirect('doctor_login')  # Redirect to your desired homepage after registration
#         else:
#             messages.error(request, 'Login failed. Please try again.')
#
#     else:
#         username = ''  # Pre-populate some fields (optional)
#         email = ''
#         first_name = ''
#         last_name = ''
#
#     context = {'departments': departments, 'username': username, 'email': email, 'first_name': first_name, 'last_name': last_name}
#     return render(request, 'doctor/registration_doctor.html', context)




# from django.contrib.auth import authenticate, login
# from django.contrib import messages
# from django.contrib.auth.models import User
#
# from django.db import IntegrityError
#
# def doctor_register(request):
#     departments = Department.objects.all()
#     if request.method == 'POST':
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         contact = request.POST['contact']
#         department_id = request.POST['department']
#         doc_spec = request.POST['doc_spec']
#         availability = request.POST['availability']
#         doc_image = request.FILES.get('doc_image')
#
#         if password1 != password2:
#             messages.error(request, 'Passwords do not match.')
#             return render(request, 'registration_doctor.html', {'departments': departments})
#
#         try:
#             user = User.objects.create_user(email, email, password1, first_name=first_name, last_name=last_name)
#             doctor = Doctor.objects.create(
#                 user=user,
#                 first_name=first_name,
#                 last_name=last_name,
#                 email=email,
#                 contact=contact,
#                 department_id=department_id,
#                 doc_spec=doc_spec,
#                 availability=availability,
#                 doc_image=doc_image,
#             )
#
#             login(request, user)
#             messages.success(request, 'Doctor registration successful!')
#             return redirect('doctor_dashboard')
#
#         except IntegrityError:
#             messages.error(request, 'A doctor with this email already exists.')
#             return render(request, 'doctor/registration_doctor.html', {'departments': departments})
#         except Exception as e:
#             messages.error(request, f'An error occurred: {e}')
#             return render(request, 'doctor/registration_doctor.html', {'departments': departments})
#
#     return render(request, 'doctor/registration_doctor.html', {'departments': departments})



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Doctor, Department
from django.db import IntegrityError

def doctor_register(request):

    list(messages.get_messages(request))
    departments = Department.objects.all()
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        contact = request.POST['contact']
        department_id = request.POST['department']
        doc_spec = request.POST['doc_spec']
        availability = request.POST['availability']
        doc_image = request.FILES.get('doc_image')

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'doctor/registration_doctor.html', {'departments': departments})

        try:
            user = User.objects.create_user(email, email, password1, first_name=first_name, last_name=last_name)
            doctor = Doctor.objects.create(
                user=user,
                first_name=first_name,
                last_name=last_name,
                email=email,
                contact=contact,
                department_id=department_id,
                doc_spec=doc_spec,
                availability=availability,
                doc_image=doc_image,
            )

            messages.success(request, 'Doctor registration successful! Please log in.')
            return redirect('doctor_login')

        except IntegrityError:
            messages.error(request, 'A doctor with this email already exists.')
            return render(request, 'doctor/registration_doctor.html', {'departments': departments})
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')
            return render(request, 'doctor/registration_doctor.html', {'departments': departments})

    return render(request, 'doctor/registration_doctor.html', {'departments': departments})


# def doctor_login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(request, username=email, password=password)
#         if user is not None and hasattr(user, 'doctor'):
#             login(request, user)
#             return redirect('doctor_dashboard')
#         else:
#             return render(request, 'doctor/login_doctor.html', {'error': 'Invalid email or password'})
#
#     return render(request, 'doctor/login_doctor.html')

def doctor_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # User authentication using email
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('doctor_dashboard')  # Redirect to your desired homepage after login
        else:
            messages.error(request, 'Invalid email or password. Please try again.')
            return render(request, 'doctor/login_doctor.html')

    return render(request, 'doctor/login_doctor.html')

def add_doctor(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        contact = request.POST['contact']
        department_id = request.POST['department']
        doc_spec = request.POST['doc_spec']
        availability = request.POST['availability']
        doc_image = request.FILES.get('doc_image')

        department = Department.objects.get(id=department_id)
        user = User.objects.create_user(username=email, email=email)
        doctor = Doctor.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            email=email,
            contact=contact,
            department=department,
            doc_spec=doc_spec,
            availability=availability,
            doc_image=doc_image
        )
        return redirect('doctor_list')

    departments = Department.objects.all()
    return render(request, 'doctor/add_doctor.html', {'departments': departments})


# def add_doctor(request):
#     if request.method == "POST":
#         first_name = request.POST["first_name"]
#         last_name = request.POST["last_name"]
#         email = request.POST["email"]
#         contact = request.POST["contact"]
#         department = request.POST["department"]
#         availability = request.POST["availability"]
#         date_joined = request.POST['date_joined']
#
#         Doctor.objects.create(
#             user=User.objects.create(username=email, email=email, first_name=first_name, last_name=last_name),
#             contact=contact,
#             department=department,
#             availability=availability,
#             date_joined=date_joined
#         )
#         return redirect("doctor_list")
#     return render(request, "doctor/add_doctor.html")

# def add_doctor(request):
#     if request.method == "POST":
#         first_name = request.POST["first_name"]
#         last_name = request.POST["last_name"]
#         email = request.POST["email"]
#         contact = request.POST["contact"]
#         department = request.POST["department"]
#         availability = request.POST["availability"]
#         date_joined = request.POST['date_joined']
#
#         Doctor.objects.create(
#             user=User.objects.create(username=email, email=email, first_name=first_name, last_name=last_name),
#             contact=contact,
#             department=department,
#             availability=availability,
#             date_joined=date_joined
#         )
#         return redirect("doctor_list")
#
#     department_choices = Doctor.DEPARTMENT_CHOICES
#     return render(request, "doctor/add_doctor.html", {
#         'department_choices': department_choices,
#     })




# def add_doctor(request):
#     if request.method == "POST":
#         # Extract form data
#         first_name = request.POST["first_name"]
#         last_name = request.POST["last_name"]
#         email = request.POST["email"]
#         contact = request.POST["contact"]
#         department = request.POST["department"]
#         availability = request.POST["availability"]
#         date_joined = request.POST['date_joined']
#
#         # Check if the user with given email already exists
#         user, created = User.objects.get_or_create(
#             email=email,
#             defaults={
#                 'username': email,
#                 'first_name': first_name,
#                 'last_name': last_name
#             }
#         )
#
#         # Create the doctor associated with the user
#         doctor = Doctor.objects.create(
#             user=user,
#             contact=contact,
#             department=department,
#             availability=availability,
#             date_joined=date_joined
#         )
#
#         return redirect("admin_doctor_list")  # Adjust the redirect URL as per your application
#     else:
#         department_choices = Doctor.DEPARTMENT_CHOICES
#         return render(request, "admin_panel/add_doctor.html", {
#             'department_choices': department_choices,
#         })

def doctor_edit_doctor(request,pk):
    doctor = Doctor.objects.get(id=pk)
    if request.method == "POST":
        doctor.first_name = request.POST['firstname']
        doctor.last_name = request.POST['last_name']
        doctor.email = request.POST['email']
        doctor.contact = request.POST['contact']
        doctor.department = request.POST['department']
        doctor.availability = request.POST['availability']
        doctor.date_joined = request.POST['date_joined']

        doctor.save()
        return redirect('doctor_list')
    return render(request, 'doctor/doctor_edit_doctor.html',{'doctor':doctor})

# def admin_edit_doctor(request, doctor_id):
#     doctor = get_object_or_404(Doctor, id=doctor_id)
#     if request.method == 'POST':
#         doctor.first_name = request.POST['first_name']
#         doctor.last_name = request.POST['last_name']
#         doctor.email = request.POST['email']
#         doctor.contact = request.POST['contact']
#         doctor.department_id = request.POST['department']
#         doctor.doc_spec = request.POST['doc_spec']
#         doctor.availability = request.POST['availability']
#         if 'doc_image' in request.FILES:
#             doctor.doc_image = request.FILES['doc_image']
#         doctor.save()
#         return redirect('admin_doctor_list')
#
#     departments = Department.objects.all()
#     return render(request, 'dashboard/admin_edit_doctor.html', {'doctor': doctor, 'departments': departments})





def admin_edit_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == 'POST':
        doctor.first_name = request.POST['first_name']
        doctor.last_name = request.POST['last_name']
        doctor.email = request.POST['email']
        doctor.contact = request.POST['contact']
        doctor.department_id = request.POST['department']  # Assuming 'department' is the name of the select field
        doctor.doc_spec = request.POST['doc_spec']
        doctor.availability = request.POST['availability']

        if 'doc_image' in request.FILES:
            doctor.doc_image = request.FILES['doc_image']

        doctor.save()
        return redirect('admin_doctor_list')

    departments = Department.objects.all()
    return render(request, 'dashboard/admin_edit_doctor.html', {'doctor': doctor, 'departments': departments})


from django.urls import reverse


#######from dahboard app ########





#
# def adminsignup(request):
#     return render(request, "dashboard/adminsignup.html")
# def adminlogin(request):
#     return render(request, "dashboard/adminlogin.html")
#
#
# def doctorsignup(request):
#     return render(request, "dashboard/doctorsignup.html")
#
# def doctorlogin(request):
#     return render(request, "dashboard/doctorlogin.html")
#
# def patientsignup(request):
#     return render(request, "dashboard/patientsignup.html")
#
# def patientlogin(request):
#     return render(request, "dashboard/patientlogin.html")
# def patientindex(request):
#     return render(request, "dashboard/index.html")


# def home(request):
#     return render(request, 'dashboard_2/home.html')

#patient views
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, "doctor/patient_list.html",{'patients': patients})

# def add_patient(request):
#     if request.method == "POST":
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         contact = request.POST['contact']
#         date_of_birth = request.POST['date_of_birth']
#         address = request.POST['address']
#         gender = request.POST['gender']
#         medical_history = request.POST['medical_history']
#
#         Patient.objects.create(
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             contact=contact,
#             date_of_birth=date_of_birth,
#             address=address,
#             gender=gender,
#             medical_history=medical_history,
#         )
#         return redirect('patient_list')
#     return render(request, "doctor/add_patient.html")


# def add_patient(request):
#     if request.method == "POST":
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         contact = request.POST['contact']
#         date_of_birth = request.POST['date_of_birth']
#         address = request.POST['address']
#         gender = request.POST['gender']
#         medical_history = request.POST['medical_history']
#
#         # Assuming the user is logged in and request.user is available
#         user = request.user
#
#         Patient.objects.create(
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             contact=contact,
#             date_of_birth=date_of_birth,
#             address=address,
#             gender=gender,
#             medical_history=medical_history,
#             user=user  # Associate the patient with the current user
#         )
#         return redirect('patient_list')
#     return render(request, "doctor/add_patient.html")



from django.shortcuts import render, redirect
from .models import Patient


def add_patient(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        contact = request.POST['contact']
        date_of_birth = request.POST['date_of_birth']
        address = request.POST['address']
        gender = request.POST['gender']
        medical_history = request.POST['medical_history']

        user = request.user

        # Check if a Patient already exists for this user
        try:
            patient = Patient.objects.get(user=user)
            # Update existing patient details
            patient.first_name = first_name
            patient.last_name = last_name
            patient.email = email
            patient.contact = contact
            patient.date_of_birth = date_of_birth
            patient.address = address
            patient.gender = gender
            patient.medical_history = medical_history
            patient.save()
        except Patient.DoesNotExist:
            # Create a new patient if one doesn't exist
            Patient.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                contact=contact,
                date_of_birth=date_of_birth,
                address=address,
                gender=gender,
                medical_history=medical_history,
                user=user
            )

        return redirect('patient_list')
    return render(request, "doctor/add_patient.html")



def edit_patient(request,pk):
    patient = Patient.objects.get(id=pk)
    if request.method == "POST":
        patient.first_name = request.POST['first_name']
        patient.last_name = request.POST['last_name']
        patient.email = request.POST['email']
        patient.contact = request.POST['contact']
        patient.date_of_birth = request.POST['date_of_birth']
        patient.address = request.POST['address']
        patient.gender = request.POST['gender']
        patient.medical_history = request.POST['medical_history']

        patient.save()
        return redirect('patient_list')
    return render(request, "doctor/edit_patient.html", {'patient': patient})


#Doctor views







#Billing views
# def billing_list(request, user=Patient):
#     user = request.user
#     billings = Billing.objects.all()
#
#
#
#     total_amount_patient = 0
#
#     # Calculate gross total amount billed across all patients
#     gross_total_amount = Billing.objects.aggregate(Sum('amount'))['amount__sum'] or 0
#
#     context = {
#         'user': user,
#         'billings': billings,
#
#         'gross_total_amount': gross_total_amount,
#     }
#     return render(request, "doctor/doctor_patient_bill.html", {'billings':billings})


# from django.db.models import F
#
# def billing_list(request, user=Patient):
#     user = request.user
#     billings = Billing.objects.annotate(
#         patient_first_name=F('patient__first_name'),
#         patient_last_name=F('patient__last_name'),
#         patient_contact=F('patient__contact'),
#         patient_email=F('patient__email'),
#         patient_date_created=F('patient__date_created')
#     )
#
#     total_amount_patient = 0
#
#     # Calculate gross total amount billed across all patients
#     gross_total_amount = Billing.objects.aggregate(Sum('amount'))['amount__sum'] or 0
#
#     context = {
#         'user': user,
#         'billings': billings,
#         'gross_total_amount': gross_total_amount,
#     }
#     return render(request, "doctor/doctor_patient_bill.html", context)


from django.db.models import F, Sum


def billing_list(request):
    user = request.user
    current_doctor = Doctor.objects.get(user=user)

    billings = Billing.objects.filter(doctor=current_doctor).annotate(
        patient_first_name=F('patient__first_name'),
        patient_last_name=F('patient__last_name'),
        patient_contact=F('patient__contact'),
        patient_email=F('patient__email'),
        patient_date_created=F('patient__date_created')
    )

    total_amount_patient = billings.aggregate(Sum('amount'))['amount__sum'] or 0

    # Calculate gross total amount billed across all patients
    gross_total_amount = Billing.objects.aggregate(Sum('amount'))['amount__sum'] or 0

    context = {
        'user': user,
        'billings': billings,
        'total_amount_patient': total_amount_patient,
        'gross_total_amount': gross_total_amount,
    }
    return render(request, "doctor/doctor_patient_bill.html", context)


def add_billing(request):
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    if request.method == "POST":
        patient_id = request.POST['patient']
        doctor_id = request.POST['doctor']
        amount = request.POST['amount']
        date = request.POST['date']
        status = request.POST['status']
        description = request.POST['description']

        patient = Patient.objects.get(id=patient_id)
        doctor = Doctor.objects.get(id=doctor_id)

        Billing.objects.create(
            patient=patient,
            doctor=doctor,
            amount=amount,
            date=date,
            status=status,
            description=description
        )
        return redirect("billing_list")
    return render(request, "doctor/add_billing.html", {'patients': patients, 'doctors': doctors})


from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Billing, Patient, Doctor
from .forms import BillingForm

@login_required()
def edit_billing(request, billing_id):
    billing = get_object_or_404(Billing, id=billing_id)
    if request.method == "POST":
        form = BillingForm(request.POST, instance=billing)
        if form.is_valid():
            form.save()
            return redirect(reverse('billing_list'))
    else:
        form = BillingForm(instance=billing)

    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    return render(request, 'doctor/edit_billing.html',
                  {'form': form, 'billing': billing, 'patients': patients, 'doctors': doctors})

def doctor_patient_bill(request):
    return render(request, "doctor/doctor_patient_bill.html")


#report views
def report(request):
    patient_count = Patient.objects.count()
    doctor_count = Doctor.objects.count()
    billing_count = Billing.objects.count()
    total_revenue = Billing.objects.filter(status='Paid').aggregate(total=models.Sum('amount'))['total'] or 0

    context = {
        'patient_count': patient_count,
        'doctor_count': doctor_count,
        'billing_count': billing_count,
        'total_revenue': total_revenue,
    }
    return render(request, 'dashboard/report.html',context)


#dashboard views
# @login_required
# def doctor_dashboard(request):
#     # if request.user.user_type != 'doctor':
#     #     return redirect('login')
#
#     return render(request, "doctor/doctor_dashboard.html")


# @login_required
# def doctor_dashboard(request):
#     user = request.user
#     return render(request, 'doctor/doctor_dashboard.html', {'user': user})



# @login_required
# def doctor_dashboard(request):
#     doctor = request.user.doctor
#     patients = Patient.objects.all()  # Assuming you want to display all patients
#     appointments = Appointment.objects.filter(doctor=doctor)  # Fetching appointments for the logged-in doctor
#
#     context = {
#         'patients': patients,
#         'appointments': appointments,
#     }
#     return render(request, 'doctor/doctor_dashboard.html', context)


@login_required
def doctor_dashboard(request):
    # Fetch the doctor instance for the logged-in user
    doctor = get_object_or_404(Doctor, user=request.user)
    # Fetch patients and appointments for this doctor
    patients = Patient.objects.all()  # Assuming you want to display all patients
    appointments = Appointment.objects.filter(doctor=doctor)  # Fetching appointments for the logged-in doctor

    context = {
        'user': request.user,
        'doctor': doctor,
        'patients': patients,
        'appointments': appointments,
    }
    return render(request, 'doctor/doctor_dashboard.html', context)


#view to handle appointment bookings
# @login_required
# def book_appointment(request):
#     if request.user.user_type != 'patient':
#         return redirect('login')
#
#     doctors = DoctorProfile.objects.select_realated('user').all()
#
#     if request.method == "POST":
#         doctor_id = request.POST['doctor']
#         date = request.POST['date']
#         time = request.POST['time']
#         symptoms = request.POST['symptoms']
#
#         doctor = User.objects.get(id=doctor_id)
#         Appointment.objects.create(patient=request.user, doctor=doctor, date=date, time=time, symptoms=symptoms)
#
#         return redirect('patient_dashboard')
#     # return render(request, 'dashboard/patient_book_appointment.html', {'doctors': doctors})
#
#     return render(request, 'patient/patient_book_appointment.html', {'doctors': doctors})




# @login_required
# def book_appointment(request):
#     try:
#         profile = Profile.objects.get(user=request.user)
#     except Profile.DoesNotExist:
#         return redirect('login')
#
#     if profile.user_type != 'patient':
#         return redirect('login')
#
#     doctors = DoctorProfile.objects.select_related('user').all()
#
#     if request.method == "POST":
#         doctor_id = request.POST['doctor']
#         date = request.POST['date']
#         time = request.POST['time']
#         symptoms = request.POST['symptoms']
#
#         doctor = User.objects.get(id=doctor_id)
#         Appointment.objects.create(patient=request.user, doctor=doctor, date=date, time=time, symptoms=symptoms)
#
#         return redirect('patient_dashboard')
#
#     return render(request, 'patient/patient_book_appointment.html', {'doctors': doctors})


# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .models import DoctorProfile, Appointment
# from django.contrib.auth.models import User
#
#
# @login_required
# def book_appointment(request):
#     if request.user.groups.filter(name='Patients').exists():
#         doctors = DoctorProfile.objects.all()  # Fetch all doctor profiles
#
#         if request.method == "POST":
#             doctor_id = request.POST.get('doctor')
#             date = request.POST.get('date')
#             time = request.POST.get('time')
#             symptoms = request.POST.get('symptoms')
#
#             doctor_profile = DoctorProfile.objects.get(pk=doctor_id)
#             doctor = doctor_profile.user  # Access the related User object
#
#             Appointment.objects.create(patient=request.user, doctor=doctor, date=date, time=time, symptoms=symptoms)
#
#             return redirect('patient_dashboard')
#
#         return render(request, 'patient/patient_book_appointment.html', {'doctors': doctors})
#
#     return redirect('login')  # Redirect to login if user is not a patient
#
# from .models import DoctorProfile  # Import your DoctorProfile model

# @login_required
# def book_appointment(request):
#     if request.user.user_type != 'patient':
#         return redirect('login')
#
#     doctors = DoctorProfile.objects.all()  # Fetch all doctors
#
#     if request.method == "POST":
#         doctor_id = request.POST['doctor']
#         date = request.POST['date']
#         time = request.POST['time']
#         symptoms = request.POST['symptoms']
#
#         # Assuming DoctorProfile has a ForeignKey to User, you can get the doctor details like this:
#         doctor = DoctorProfile.objects.get(id=doctor_id)
#         Appointment.objects.create(patient=request.user, doctor=doctor.user, date=date, time=time, symptoms=symptoms)
#
#         return redirect('patient_dashboard')
#
#     return render(request, 'patient/patient_book_appointment.html', {'doctors': doctors})




# @login_required
# def book_appointment(request):
#     try:
#         profile = request.user.profile
#         if profile.user_type != 'patient':
#             return redirect('patient_login')  # Redirect to patient login if user is not a patient
#     except Profile.DoesNotExist:
#         return redirect('patient_login')  # Redirect to patient login if user profile doesn't exist
#
#     doctors = DoctorProfile.objects.all()  # Fetch all doctors
#
#     if request.method == "POST":
#         doctor_id = request.POST.get('doctor')
#         # Example: Process form submission
#         print(f"Doctor ID selected: {doctor_id}")
#         # Add logic to save appointment, handle validation, etc.
#
#     context = {
#         'doctors': doctors,
#     }
#     return render(request, 'patient/book_appointment.html', context)
#


# hospital/views.py

# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .models import DoctorProfile, Appointment
# from .forms import BookAppointmentForm
#
# @login_required
# def book_appointment(request):
#     # Check if the user is a patient
#     if not hasattr(request.user, 'patient'):
#         return redirect('patient_login')  # Redirect to patient login if user is not a patient
#
#     form = BookAppointmentForm(request.POST or None)
#
#     if request.method == "POST":
#         if form.is_valid():
#             doctor_id = form.cleaned_data['doctor']
#             appointment_date = form.cleaned_data['appointment_date']
#             doctor = DoctorProfile.objects.get(pk=doctor_id)
#             appointment = Appointment.objects.create(patient=request.user.patient, doctor=doctor, appointment_date=appointment_date)
#             appointment.save()
#             return redirect('patient_dashboard')  # Redirect after successful booking
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'patient/patient_book_appointment.html', context)



@login_required
def admin_dashboard(request):
    patient_count = Patient.objects.count()
    doctor_count = Doctor.objects.count()
    billing_count = Billing.objects.count()
    total_revenue = Billing.objects.filter(status='Paid').aggregate(total=models.Sum('amount'))['total'] or 0

    context2 = {
        'patient_count': patient_count,
        'doctor_count': doctor_count,
        'billing_count': billing_count,
        'total_revenue': total_revenue,
    }
    return render(request, 'dashboard/admin_dashboard.html',context2)
# @login_required
# def admin_dashboard(request):
#     return render(request, 'admin_panel/index.html')

@login_required
def admin_patient_list(request):
    patients = Patient.objects.all()
    return render(request, "dashboard/admin_patient_list.html", {'patients': patients})
# def doctor_list(request):
#     doctors = Doctor.objects.all()
#     return render(request, 'doctor/admin_doctor_list.html', {'doctors': doctors})

def admin_billing_list(request):
    billings = Billing.objects.all()
    return render(request, 'dashboard/admin_billing_list.html', {'billings': billings})



def admin_add_patient(request):
    if request.method == "POST":
        # Retrieve form data
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST['email']
        contact = request.POST['contact']
        date_of_birth = request.POST['date_of_birth']
        address = request.POST['address']
        gender = request.POST['gender']
        medical_history = request.POST["medical_history"]

        # Retrieve the user object (assuming the user is already logged in)
        user = request.user

        # Ensure the user is not anonymous before creating a Patient
        if user.is_authenticated:
            # Create a new Patient object and save it to the database
            Patient.objects.create(
                user=user,  # Add the user to the patient
                first_name=first_name,
                last_name=last_name,
                email=email,
                contact=contact,
                date_of_birth=date_of_birth,
                address=address,
                gender=gender,
                medical_history=medical_history
            )

            # Redirect to the patient list page after the patient is added
            return redirect('admin_patient_list')

    # Render the add patient form template if it's not a POST request
    return render(request, 'dashboard/admin_add_patient.html')



# def admin_add_doctor(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         contact = request.POST['contact']
#         department = request.POST['department']
#         availability = request.POST['availability']
#         date_joined = request.POST['date_joined']
#
#         Doctor.objects.create(
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             contact=contact,
#             department=department,
#             availability=availability,
#             date_joined=date_joined
#         )
#         return redirect('admin_doctor_list')
#     return render(request, 'dashboard/admin_add_doctor.html')
#


# def admin_add_doctor(request):
#     if request.method == "POST":
#         # Extract form data
#         first_name = request.POST["first_name"]
#         last_name = request.POST["last_name"]
#         email = request.POST["email"]
#         contact = request.POST["contact"]
#         department = request.POST["department"]
#         availability = request.POST["availability"]
#         date_joined = request.POST['date_joined']
#
#         # Check if the user with given email already exists
#         user, created = User.objects.get_or_create(
#             email=email,
#             defaults={
#                 'username': email,
#                 'first_name': first_name,
#                 'last_name': last_name
#             }
#         )
#
#         # Create the doctor associated with the user
#         doctor = Doctor.objects.create(
#             user=user,
#             contact=contact,
#             department=department,
#             availability=availability,
#             date_joined=date_joined
#         )
#
#         return redirect("admin_doctor_list")  # Adjust the redirect URL as per your application
#     # else:
#     #     department_choices = Doctor.DEPARTMENT_CHOICES
#     return render(request, "dashboard/admin_add_doctor.html", {
#             # 'department_choices': department_choices,
#         })

# from .forms import DoctorForm
#
# #for form.py
# def admin_add_doctor(request):
#     if request.method == 'POST':
#         form = DoctorForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('doctor_list')  # Redirect to the doctor list after saving
#     else:
#         form = DoctorForm()
#     departments = Department.objects.all()
#     return render(request, 'dashboard/admin_add_doctor.html', {'form': form, 'departments': departments})

# def admin_add_doctor(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         contact = request.POST['contact']
#         department_id = request.POST['department']
#         doc_spec = request.POST['doc_spec']
#         availability = request.POST['availability']
#         doc_image = request.FILES.get('doc_image')
#
#         # Debugging: Print received data
#
#         print("Received data:", first_name, last_name, email, contact, department_id, doc_spec, availability, doc_image)
#
#
#         department = Department.objects.get(id=department_id)
#
#         Doctor.objects.create(
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             contact=contact,
#             department=department,
#             doc_spec=doc_spec,
#             availability=availability,
#             doc_image=doc_image
#         )
#         return redirect('doctor_list')  # Redirect to the doctor list after saving
#
#     departments = Department.objects.all()
#     return render(request, 'dashboard/admin_add_doctor.html', {'departments': departments})





# def admin_add_doctor(request):
#     if request.method == 'POST':
#         # Assuming user_id is passed via form or inferred (e.g., logged-in user)
#         user_id = request.POST.get('user_id')  # Example: Get user_id from form
#         user = User.objects.get(id=user_id)
#
#         # Retrieve other form fields
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         contact = request.POST['contact']
#         department_id = request.POST['department']
#         doc_spec = request.POST['doc_spec']
#         availability = request.POST['availability']
#         doc_image = request.FILES.get('doc_image')
#
#         department = Department.objects.get(id=department_id)
#
#         # Check if a doctor with the same user_id already exists
#         # existing_doctor = Doctor.objects.filter(user=user)
#         # if existing_doctor.exists():
#         #     # Handle case where doctor with the same user_id already exists
#         #     # You may redirect or render an error message here
#         #     return render(request, 'dashboard/error.html', {'message': 'Doctor with this user already exists'})
#
#         # Create a new Doctor object
#         Doctor.objects.create(
#             user=user,
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             contact=contact,
#             department=department,
#             doc_spec=doc_spec,
#             availability=availability,
#             doc_image=doc_image
#         )
#         return redirect('admin_doctor_list')  # Redirect to the doctor list view
#
#     departments = Department.objects.all()
#     return render(request, 'dashboard/admin_add_doctor.html', {'departments': departments})


def admin_add_doctor(request):
    if request.method == 'POST':
        # Assuming user_id is passed via form or inferred (e.g., logged-in user)
        user_id = request.POST.get('user_id')  # Example: Get user_id from form
        user = User.objects.get(id=user_id)

        # Retrieve other form fields
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        contact = request.POST['contact']
        department_id = request.POST['department']
        doc_spec = request.POST['doc_spec']
        availability = request.POST['availability']
        doc_image = request.FILES.get('doc_image')
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            departments = Department.objects.all()
            return render(request, 'dashboard/admin_add_doctor.html', {
                'departments': departments,
                'error': 'Passwords do not match'
            })

        department = Department.objects.get(id=department_id)

        try:
            # Check if a user with the email already exists
            if User.objects.filter(username=email).exists():
                raise IntegrityError("User with this email already exists")

            # Create a new User object for the doctor
            doctor_user = User.objects.create(
                username=email,
                email=email,
                password=make_password(password)
            )

            # Create a new Doctor object
            Doctor.objects.create(
                user=doctor_user,
                first_name=first_name,
                last_name=last_name,
                email=email,
                contact=contact,
                department=department,
                doc_spec=doc_spec,
                availability=availability,
                doc_image=doc_image
            )

            return redirect('admin_doctor_list')  # Redirect to the doctor list view

        except IntegrityError as e:
            departments = Department.objects.all()
            return render(request, 'dashboard/admin_add_doctor.html', {
                'departments': departments,
                'error': str(e)
            })

    departments = Department.objects.all()
    return render(request, 'dashboard/admin_add_doctor.html', {'departments': departments})

def admin_doctor_list(request):
    doctors = Doctor.objects.all()  # Example queryset, adjust as per your model logic
    return render(request, 'dashboard/admin_doctor_list.html', {'doctors': doctors})



def admin_add_billing(request):
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    if request.method == 'POST':
        patient_id = request.POST['patient']
        doctor_id = request.POST['doctor']
        amount = request.POST['amount']
        date = request.POST['date']
        status = request.POST['status']
        description = request.POST['description']

        Billing.objects.create(
            patient_id=patient_id,
            doctor_id=doctor_id,
            amount=amount,
            date=date,
            status=status,
            description=description
        )
        return redirect('admin_billing_list')
    return render(request, 'dashboard/admin_add_billing.html', {'patients': patients, 'doctors': doctors})




def admin_edit_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        patient.first_name = request.POST['first_name']
        patient.last_name = request.POST['last_name']
        patient.email = request.POST['email']
        patient.contact = request.POST['contact']
        patient.date_of_birth = request.POST['date_of_birth']
        patient.address = request.POST['address']
        patient.gender = request.POST['gender']
        patient.medical_history = request.POST['medical_history']
        patient.save()
        return redirect('admin_patient_list')
    return render(request, "dashboard/admin_edit_patient.html", {'patient': patient})









def admin_edit_billing(request, pk):
    billing = get_object_or_404(Billing, pk=pk)
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()

    if request.method == "POST":
        billing.patient_id = request.POST.get('patient')
        billing.doctor_id = request.POST.get('doctor')
        billing.amount = request.POST.get('amount')
        billing.date = request.POST.get('date')
        billing.status = request.POST.get('status')
        billing.description = request.POST.get('description')
        billing.save()
        return redirect('admin_billing_list')

    return render(request, "dashboard/admin_edit_billing.html",
                  {'billing': billing, 'patients': patients, 'doctors': doctors})



from django.contrib.auth.hashers import make_password


def admin_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if not Admin.objects.filter(username=username).exists():
                # Create the admin_panel instance
                admin_instance = Admin.objects.create(username=username, email=email, password=make_password(password1))
                messages.success(request, 'Admin registration successful. Please log in.')
                return redirect('admin_login')
            else:
                messages.error(request, 'Username already exists. Please choose a different one.')
                return render(request, 'dashboard/registration_admin.html', {'error': 'Username already exists'})
        else:
            messages.error(request, 'Passwords do not match. Please try again.')
            return render(request, 'dashboard/registration_admin.html', {'error': 'Passwords do not match'})

    return render(request, 'dashboard/registration_admin.html')


# def admin_register(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#
#         if password1 == password2:
#             user = User.objects.create(username=email, email=email, first_name=first_name, last_name=last_name, password=make_password(password1))
#             Admin.objects.create(user=user, first_name=first_name, last_name=last_name, email=email)
#             return redirect('admin_login')
#         else:
#             # Passwords don't match, handle this case accordingly
#             return render(request, 'dashboard/registration_admin.html', {'error': 'Passwords do not match'})
#
#     return render(request, 'dashboard/registration_admin.html')

####LOGIN VIEWS####







from . import forms

def admin_signup(request):
    form=forms.AdminSigupForm()
    if request.method=='POST':
        form=forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect('admin_login')
    return render(request,'dashboard/registration_admin.html',{'form':form})


# def admin_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         admin = Admin.objects.filter(username=username).first()
#         if admin and check_password(password, admin.password):
#             # Admin authentication successful, redirect to admin_panel dashboard
#             return redirect('panel_index')
#         else:
#             # Admin authentication failed, provide an error message
#             return render(request, 'dashboard/login_admin.html', {'error': 'Invalid username or password'})




def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'dashboard/login_admin.html')


def panel_index(request):
    print("Panel index view called")
    return render(request, 'admin_panel/index.html')

def logout_view(request):
    logout(request)
    return redirect('dashboardhome')
    # Redirect to dashboard_base.html
    # return render(request, "dashboard/dashboard_base.html")


# from django.shortcuts import redirect
# from django.contrib.auth import logout as auth_logout
# from django.views.decorators.http import require_http_methods
#
# #
# @require_http_methods(["GET", "POST"])
# def logout_view(request):
#     if request.method == 'POST':
#         # Perform logout action
#         auth_logout(request)
#         # Redirect to the desired URL after logout
#         return redirect('home')  # Change 'home' to the desired URL name
#
#     # If it's a GET request, render a page or perform other actions if needed
#     # For example, you could render a confirmation page
#     return render(request, 'logout_confirmation.html')
#




from django.shortcuts import render, redirect, get_object_or_404
from .models import Department, Doctor


def department_list(request):
    departments = Department.objects.all()
    return render(request, 'dashboard/admin_department_list.html', {'departments': departments})

# def add_department(request):
#     if request.method == 'POST':
#         form = DepartmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('department_list')
#     else:
#         form = DepartmentForm()
#     return render(request, 'dashboard/admin_add_department.html', {'form': form})

def add_department(request):
    if request.method == 'POST':
        dep_name = request.POST.get('dep_name')
        dep_description = request.POST.get('dep_description')

        if dep_name and dep_description:
            Department.objects.create(dep_name=dep_name, dep_description=dep_description)
            return redirect('department_list')

    return render(request, 'dashboard/admin_add_department.html')




# def edit_department(request, pk):
#     department = get_object_or_404(Department, pk=pk)
#     if request.method == 'POST':
#         form = DepartmentForm(request.POST, instance=department)
#         if form.is_valid():
#             form.save()
#             return redirect('department_list')  # Redirect to the department list after saving
#     else:
#         form = DepartmentForm(instance=department)
#     return render(request, 'dashboard/admin_edit_department.html', {'form': form})


def edit_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        dep_name = request.POST.get('dep_name')
        dep_description = request.POST.get('dep_description')

        if dep_name and dep_description:
            department.dep_name = dep_name
            department.dep_description = dep_description
            department.save()
            return redirect('department_list')  # Redirect to the department list after saving
    else:
        dep_name = department.dep_name
        dep_description = department.dep_description

    return render(request, 'dashboard/admin_edit_department.html', {
        'dep_name': dep_name,
        'dep_description': dep_description
    })

@login_required
def admin_delete_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        # Assuming you want to delete via POST request for safety
        doctor.delete()
        return redirect('admin_doctor_list')  # Replace with the URL name for doctor list view
    return render(request, 'dashboard/admin_confirm_delete_doctor.html', {'doctor': doctor})
@login_required
def admin_delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'dashboard/admin_confirm_delete_department.html', {'department': department})
@login_required
def admin_edit_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.first_name = request.POST.get('first_name')
        patient.last_name = request.POST.get('last_name')
        patient.email = request.POST.get('email')
        patient.contact = request.POST.get('contact')
        if patient.first_name and patient.last_name and patient.email and patient.contact:
            patient.save()
            return redirect('admin_patient_list')
    return render(request, 'dashboard/admin_edit_patient.html', {'patient': patient})

@login_required
def admin_delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('admin_patient_list')
    return render(request, 'dashboard/admin_confirm_delete_patient.html', {'patient': patient})
@login_required
def logout_confirmation(request):
    return render(request, 'dashboard/logout_confirmation.html')


@login_required
def patient_logout_confirmation(request):
    return render(request, 'patient/patient_logout_confirmation.html')


@login_required
def doctor_logout_confirmation(request):
    return render(request, 'doctor/doctor_logout_confirmation.html')



#FOR APPOINTMENT:(PATIENT)


@login_required
def patient_book_appointment(request):
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')
        symptoms = request.POST.get('symptoms')

        doctor = get_object_or_404(Doctor, id=doctor_id)
        patient = get_object_or_404(Patient, user=request.user)

        Appointment.objects.create(
            patient=patient,
            doctor=doctor,
            date=date,
            time=time,
            symptoms=symptoms
        )
        return redirect('patient_appointment_list')

    doctors = Doctor.objects.all()
    return render(request, 'patient/patient_book_appointment.html', {'doctors': doctors})

# @login_required
# def patient_appointment_list(request):
#     patient = get_object_or_404(Patient, user=request.user)
#     appointments = Appointment.objects.filter(patient=patient)
#     return render(request, 'patient/patient_appointment_list.html', {'appointments': appointments})


@login_required
def patient_appointment_list(request):
    patient = get_object_or_404(Patient, user=request.user)
    appointments = Appointment.objects.filter(patient=patient)
    print(appointments)  # Add this line to debug
    return render(request, 'patient/patient_appointment_list.html', {'appointments': appointments})




@login_required
def patient_delete_appointment(request, pk):
  appointment = Appointment.objects.get(pk=pk)
  if request.method == 'POST':
    appointment.delete()
    return redirect('patient_appointment_list')  # Replace 'appointments' with relevant URL name
  return render(request, 'patient/patient_confirm_delete_appointment.html', {'appointment': appointment})  # Confirmation template

# @login_required
# def patient_edit_appointment(request, pk):
#   appointment = Appointment.objects.get(pk=pk)
#   # ... Logic to handle editing appointment (form handling, saving changes)
#   return redirect('patient_appointment_list')


@login_required
def patient_edit_appointment(request, pk):
  appointment = Appointment.objects.get(pk=pk)
  if request.method == 'POST':
    # Extract data from the request.POST dictionary
    doctor = request.POST.get('doctor')
    date = request.POST.get('date')
    time = request.POST.get('time')
    symptoms = request.POST.get('symptoms')

    # Validation (optional, implement as needed)
    # ... validation logic ...

    # Update appointment object
    appointment.doctor_id = doctor  # Assuming doctor is a foreign key ID
    appointment.date = date
    appointment.time = time
    appointment.symptoms = symptoms
    appointment.save()

    return redirect('patient_appointment_list')  # Replace with relevant URL name
  else:
    # Pre-fill form data (context for template)
    context = {
      'appointment': appointment,
      'doctor_choices': Appointment.objects.values_list('doctor__id', 'doctor__user__first_name'),  # Replace with appropriate doctor selection logic
    }
  return render(request, 'patient/patient_edit_appointment.html', context)





# def patient_discharge(request, patient_id):
#     patient = Patient.objects.get(pk=patient_id)
#     discharge_summary, created = DischargeSummary.objects.get_or_create(patient=patient)
#
#     if request.method == 'POST':
#         discharge_summary.discharge_date = request.POST['discharge_date']
#         discharge_summary.diagnosis = request.POST['diagnosis']
#         discharge_summary.treatment_provided = request.POST['treatment_provided']
#         discharge_summary.medication_instructions = request.POST['medication_instructions']
#         discharge_summary.follow_up_instructions = request.POST['follow_up_instructions']
#         discharge_summary.doctor_notes = request.POST.get('doctor_notes', '')  # Optional
#         discharge_summary.save()
#
#         messages.success(request, 'Discharge summary saved successfully!')
#         return redirect('patient_list')  # Redirect to patient list after saving
#
#     context = {'patient': patient, 'discharge_summary': discharge_summary}
#     return render(request, 'doctor/patient_discharge.html', context)



# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .models import Patient, Doctor, Discharge

@login_required
def discharge_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    doctor = get_object_or_404(Doctor, user=request.user)

    if request.method == 'POST':
        discharge_date = request.POST.get('discharge_date')
        discharge_reason = request.POST.get('discharge_reason')
        discharge_note = request.POST.get('discharge_note')

        discharge = Discharge.objects.create(
            patient=patient,
            doctor=doctor,
            discharge_date=discharge_date,
            discharge_reason=discharge_reason,
            discharge_note=discharge_note
        )
        discharge.save()
        return redirect('patient_list')

    return render(request, 'doctor/patient_discharge.html', {'patient': patient})

@login_required
def discharge_list(request):
    doctor = get_object_or_404(Doctor, user=request.user)
    discharges = Discharge.objects.filter(doctor=doctor)
    return render(request, 'doctor/discharge_list.html', {'discharges': discharges})

@login_required
def discharge_detail(request, discharge_id):
    discharge = get_object_or_404(Discharge, id=discharge_id)
    print(discharge.patient.email)
    return render(request, 'doctor/discharge_detail.html', {'discharge': discharge})