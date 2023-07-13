from django.shortcuts import render, redirect
from django.views.generic import CreateView
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from . import forms
from .models import Patient, Emotion
from elasticsearch import Elasticsearch
# from django.conf import settings
from .models import Text
from transformers import pipeline
from datetime import datetime, timedelta
from django.db import models
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile


# es = Elasticsearch(hosts=settings.ELASTICSEARCH_HOSTS)
es = Elasticsearch([{'host': 'localhost', 'port':9200, 'scheme':'http'}])

import requests

API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-emotion-multilabel-latest"
headers = {"Authorization": f"Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def page_home(request):
    return render(request,'pages_main/home.html')



def add_text(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        patient = request.user  # Get the logged-in patient

        es = Elasticsearch([{'host': 'localhost', 'port':9200, 'scheme':'http'}])
        es.indices.refresh(index='notes2')
        # Save the text in Elasticsearch
        # Assuming you have set up the Elasticsearch connection as described earlier


        # # Evaluate the text using the Hugging Face model
        # # evaluation_result = evaluate_text(content)  # Implement this function using the Hugging Face model

        # classifier = pipeline("sentiment-analysis", model="michellejieli/emotion_text_classifier")
        # evaluation_result = classifier(content)[0]  # Implement this function using the Hugging Face model

        evaluation_result = query({"inputs": content})

        es.index(index='notes2', body={
            'patient_id': patient.id,
            'content': content,
            'emotion' : evaluation_result#[0][0]['label']
        })

        return render(request, 'pages_main/text_added.html')

    return render(request, 'pages_main/add_text.html')




def search_text(request):
    return render(request,'pages_main/search_text.html')



def text_added(request):
    return render(request, 'pages_main/text_added.html')


class SignupPage(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Créer un profil d'utilisateur pour le psychologue
        user = form.save()
        profile = UserProfile.objects.create(user=user, statut='psychologue')
        
        return response
    

def create_patient(request):
    if request.method == 'POST':
        firstname = request.POST.get('patient-firstname')
        lastname = request.POST.get('patient-lastname')
        password = request.POST.get('patient-password')
        
        # Récupérer l'utilisateur (psychologue) actuellement connecté
        psychologue = request.user

        # Créer un nouvel utilisateur avec le nom d'utilisateur et le mot de passe fournis
        user = User.objects.create_user(username=firstname, password=password)

        # Créer une instance de UserProfile associée à l'utilisateur avec le statut "patient"
        user_profile = UserProfile.objects.create(user=user, statut='patient')

        # Créer un nouveau patient lié à l'utilisateur et au psychologue
        patient = Patient.objects.create(lastname=lastname, firstname=firstname, password=password, psychologue=psychologue)

        return render(request, 'pages_main/redirect_home.html')
    else:
        return render(request, 'pages_main/new_patient.html')
    



def client_list(request):
    clients = Patient.objects.all()
    return render(request, 'pages_main/client_list.html', {'clients': clients})




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

def emotion_distribution(request):
    # Définissez la période de temps souhaitée
    start_date = datetime.now() - timedelta(days=30)
    end_date = datetime.now()

# Récupérez les émotions des patients actifs pour la période spécifiée
    active_patients = Patient.objects.filter(is_active=True)    
    emotions = Emotion.objects.filter(patient__in=active_patients, date__range=(start_date, end_date))

    # Calculez la répartition des émotions
    emotion_counts = emotions.values('evaluation').annotate(count=models.Count('evaluation'))

    # Préparez les données pour l'affichage dans le template
    emotion_data = [{'emotion': item['evaluation'], 'count': item['count']} for item in emotion_counts]

    # Renvoyez les émotions et les données au template pour l'affichage
    return render(request, 'pages_main/emotion_distribution.html', {'emotions': emotions, 'emotion_data': emotion_data})



def login_view(request):
    if request.user.is_authenticated:

        if request.user.userprofile.statut == 'psychologue':
            return render(request, 'pages_main/psyco_home.html')
        elif request.user.userprofile.statut == 'patient':
            return redirect('/patient')
    else:
        # Gérer l'authentification invalide
    #     return redirect('login')
    # else:
        return redirect('/')




@login_required(login_url='psyco_home/')
def psyco_home(request):
    if request.user.userprofile.statut == 'psychologue':
        return render(request, 'pages_main/psyco_home.html')   
    else:
        return render(request, 'pages_main/access_denied.html')
    



@login_required(login_url='patient/')
def patient_dashboard(request):
    if request.user.userprofile.statut == 'patient':
        return render(request, 'pages_main/patient_home.html')
    
    else:
        return render(request, 'pages_main/access_denied.html')
    
