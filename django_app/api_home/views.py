from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from . import forms
from .models import Patient


def login(request):
    return render(request,'pages_main/login.html')

def page_home(request):
    return render(request,'pages_main/home.html')

def new_patient(request):
    return render(request,'pages_main/new_patient.html')

def new_text(request):
    return render(request,'pages_main/new_text.html')

def search_text(request):
    return render(request,'pages_main/search_text.html')

# @login_required
# def recipe_rslt (request):
#     form = TestForm(request.POST)
#     return render(request, 'pages_main/final_recipe.html', context = form.resultat)


def psyco_home(request):
    return render(request,'pages_main/psyco_home.html')

class SignupPage(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'



def create_patient(request):
    if request.method == 'POST':
        firstname = request.POST.get('patient-firstname')
        lastname = request.POST.get('patient-lastname')
        password = request.POST.get('patient-password')
        patient = Patient.objects.create(lastname=lastname, firstname=firstname, password=password)
        patient.save()
        

        return render(request, 'pages_main/redirect_home.html')
    else:
        return render(request, 'pages_main/new_patient.html')



def client_list(request):
    clients = Patient.objects.all()
    return render(request, 'pages_main/client_list.html', {'clients': clients})


from django.shortcuts import render
from .models import Patient

def search_patient(request):
    lastname = request.GET.get('lastname', '')
    if lastname:
        patients = Patient.objects.filter(lastname__icontains=lastname)
    else:
        patients = []
    return render(request, 'pages_main/search_patient.html', {'patients': patients})


def search_results(request):
    lastname = request.GET.get('lastname', '')
    if lastname:
        patients = Patient.objects.filter(lastname__icontains=lastname)
    else:
        patients = []
    return render(request, 'pages_main/search_results.html', {'patients': patients})
