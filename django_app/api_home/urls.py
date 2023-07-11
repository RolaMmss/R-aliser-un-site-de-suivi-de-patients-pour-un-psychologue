from django.urls import path
from . import views


app_name = "api_home"

urlpatterns = [
    path('test/', views.login),   #api est nom de l'application definit sur views
    path('', views.page_home, name ='home'),
    path('new_patient/', views.psyco, name ='new_patient'),
    #path('special/', views.create_recipe, name='special'),
    path('signup/', views.SignupPage.as_view(), name='signup'),
   # path('recipe/', views.recipe_rslt),
]

