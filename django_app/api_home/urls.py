from django.urls import path
from . import views


app_name = "api_home"

urlpatterns = [
    path('test/', views.login),   #api est nom de l'application definit sur views
    path('', views.page_home, name ='home'),
    path('create_patient/', views.create_patient, name ='create_patient'),
    path('new_text/', views.new_text, name ='new_text'),
    path('search_text/', views.search_text, name ='search_text'),
    path('psyco_home/', views.psyco_home, name ='psyco_home'),
    path('client_list/', views.client_list, name='client_list'),



    #path('special/', views.create_recipe, name='special'),
    path('signup/', views.SignupPage.as_view(), name='signup'),
   # path('recipe/', views.recipe_rslt),
]
