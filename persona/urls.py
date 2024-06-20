from django.urls import path
from persona import views


urlpatterns = [
  
    path("", views.inicio, name="inicio"),
   
 ]
