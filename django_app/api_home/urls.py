from django.urls import path
from . import views



app_name = "api_home"

urlpatterns = [
   
    path('', views.page_home, name ='home'),
    path('create_patient/', views.create_patient, name ='create_patient'),
    path('add-text/', views.add_text, name='add-text'),
    path('text-added/', views.text_added, name='text-added'),
    path('search_text/', views.search_text, name ='search_text'),


    path('psyco_home/', views.psyco_home, name ='psyco_home'),
    path('client_list/', views.client_list, name='client_list'),
    path('search_patient/', views.search_patient, name='search_patient'),
    path('search_results/', views.search_results, name='search_results'),

    
    path('patient/', views.patient_dashboard, name='patient_dashboard'),

    path('login_view/', views.login_view, name='login_view'),

    path('emotion_distribution/', views.emotion_distribution, name='emotion_distribution-visualization'),

    #path('special/', views.create_recipe, name='special'),
    path('signup/', views.SignupPage.as_view(), name='signup'),
   # path('recipe/', views.recipe_rslt),
]
