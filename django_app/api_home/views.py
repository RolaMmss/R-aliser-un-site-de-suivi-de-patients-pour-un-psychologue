from django.shortcuts import render
# from .forms import IngredientsForm, TestForm
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from . import forms

def login(request):
    return render(request,'pages_main/login.html')

def page_home(request):
    return render(request,'pages_main/home.html')



# @login_required
# def recipe_rslt (request):
#     form = TestForm(request.POST)
#     return render(request, 'pages_main/final_recipe.html', context = form.resultat)

class SignupPage(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'