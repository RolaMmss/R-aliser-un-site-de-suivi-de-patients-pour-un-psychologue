from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings
from suivi_app.models import User, Rdv
from django.contrib import messages
from datetime import datetime



def accueil(request):
    """Vue pour la page d'accueil du site. Affiche des statistiques sur les rendez-vous
    à venir et les créneaux horaires libres si le coach est connecté. Sinon il affiche la présentation du coach et ses prestations.

    Args:
        request : requête HTTP reçue par la vue

    Returns:
        - réponse HTTP avec un template rendu contenant les statistiques suivantes pour le coach :
            - le nombre de rendez-vous à venir 
            - le nombre de créneaux horaires libres
            - la date courante au format 'YYYY-MM-DD'
            - l'heure courante au format 'HH:MM'
    """
    today = datetime.now().date()
    rdv_a_venir = Rdv.objects.filter(date__gte=today, user__isnull=False)
    rdv_count = rdv_a_venir.count()
    creneaux_libres = Rdv.objects.filter(date__gte=today, user__isnull=True)
    creneaux_libres_count = creneaux_libres.count()
    now = datetime.now()
    hour = now.strftime("%H:%M")
    return render(request, 'rdv/accueil.html',{'rdv_count':rdv_count, 'creneaux_libres_count':creneaux_libres_count, 'today':today, 'hour':hour})


def login_page(request):
    """
    Vue pour la page de connexion du site. Permet à un utilisateur de se connecter avec son nom d'utilisateur
    et son mot de passe, puis redirige l'utilisateur vers la page d'accueil si les informations de connexion
    sont valides.

    Parameters:
    - request: requête HTTP reçue par la vue

    Returns:
    - réponse HTTP avec un template rendu contenant un formulaire de connexion et un message d'erreur (si applicable)
      - si le formulaire est soumis et valide, l'utilisateur est authentifié et redirigé vers la page d'accueil
      - sinon, le formulaire est réaffiché avec un message d'erreur indiquant que les identifiants sont invalides
    """
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('accueil')
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'rdv/login.html', context={'form': form, 'message': message})


@login_required(login_url='login')
def logout_user(request):
    """
    Vue pour la déconnexion de l'utilisateur connecté. Déconnecte l'utilisateur actuel et le redirige vers la
    page d'accueil.

    Parameters:
    - request: requête HTTP reçue par la vue

    Returns:
    - réponse HTTP avec une redirection vers la page d'accueil
    """
    logout(request)
    return redirect('accueil')


def signup_page(request):
    """
    Vue pour la page d'inscription du site. Affiche un formulaire d'inscription permettant à un nouvel utilisateur
    de créer un compte. Si le formulaire est soumis et valide, le nouvel utilisateur est enregistré et connecté automatiquement, puis redirigé vers la
    page d'accueil.

    Parameters:
    - request: requête HTTP reçue par la vue

    Returns:
    - réponse HTTP avec un template rendu contenant un formulaire d'inscription
      - si le formulaire est soumis et valide, un nouvel utilisateur est créé et connecté, puis l'utilisateur est
        redirigé vers la page d'accueil
      - sinon, le formulaire est réaffiché avec les erreurs de validation appropriées
    """
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accueil')
    return render(request, 'rdv/signup.html', {'form':form})


# @login_required(login_url='login')