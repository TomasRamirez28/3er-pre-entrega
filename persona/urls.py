from django.urls import path
from persona import views


urlpatterns = [
  
    path("", views.inicio, name="inicio"),
    path('datos_persona/', views.datos_persona, name='datos_persona'),
    path('lista_persona/', views.lista_persona, name='lista_persona'),  
   
 ]
