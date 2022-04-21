from  django.urls import path
from django.views import View
from AppOne import views


urlpatterns = [
   
   
 path('integrantes/', views.integrantes),
 path('empleo/', views.empleo),
 path('entretenimiento/', views.entretenimiento),
 path('', views.inicio),
    
]
