from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from . import forms
from .models import Patient, Emotion
from elasticsearch import Elasticsearch
from django.conf import settings
from .models import Text
from transformers import pipeline
from datetime import datetime, timedelta


# es = Elasticsearch(hosts=settings.ELASTICSEARCH_HOSTS)
es = Elasticsearch([{'host': 'localhost', 'port':9200, 'scheme':'http'}])


def login(request):
    return render(request,'pages_main/login.html')

def page_home(request):
    return render(request,'pages_main/home.html')

# def new_patient(request):
#     return render(request,'pages_main/new_patient.html')

def add_text(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        patient = request.user  # Get the logged-in patient

        # Save the text in Elasticsearch
        # Assuming you have set up the Elasticsearch connection as described earlier
        es.index(index='texts', body={
            'patient_id': patient.id,
            'content': content,
        })

        # Evaluate the text using the Hugging Face model
        # evaluation_result = evaluate_text(content)  # Implement this function using the Hugging Face model

        classifier = pipeline("sentiment-analysis", model="michellejieli/emotion_text_classifier")
        evaluation_result = classifier(content)[0]  # Implement this function using the Hugging Face model

        # Save the text and evaluation in the database
        text = Text(patient=patient, content=content, evaluation=evaluation_result)
        text.save()

        return redirect('text_added')  # Redirect to a success page

    return render(request, 'pages_main/add_text.html')

def search_text(request):
    return render(request,'pages_main/search_text.html')

# @login_required
# def recipe_rslt (request):
#     form = TestForm(request.POST)
#     return render(request, 'pages_main/final_recipe.html', context = form.resultat)

def text_added(request):
    return render(request, 'pages_main/text_added.html')


class SignupPage(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'



def create_patient(request):
    if request.method == 'POST':
        firstname = request.POST.get('patient-firstname')
        lastname = request.POST.get('patient-lastname')
        password = request.POST.get('patient-password')
        
        patient = Patient.objects.create(nom=lastname, prenom=firstname, password=password)
        patient.save()
        
        # Redirigez vers une autre page ou effectuez une autre action
        # Redirigez vers une autre page en utilisant un lien avec href
        return render(request, 'pages_main/redirect_home.html')
    else:
        return render(request, 'pages_main/new_patient.html')

def emotion_distribution(request):
    # Définissez la période de temps souhaitée
    start_date = datetime.now() - timedelta(days=30)
    end_date = datetime.now()

    # Récupérez les émotions des patients actifs pour la période spécifiée
    emotions = Emotion.objects.filter(patient__is_active=True, date__range=(start_date, end_date))

    # Calculez la répartition des émotions
    emotion_counts = emotions.values('evaluation').annotate(count=models.Count('evaluation'))

    # Préparez les données pour l'affichage dans le template
    emotion_data = [{'emotion': item['evaluation'], 'count': item['count']} for item in emotion_counts]

    # Renvoyez les émotions et les données au template pour l'affichage
    return render(request, 'pages_main/emotion_distribution.html', {'emotions': emotions, 'emotion_data': emotion_data})
