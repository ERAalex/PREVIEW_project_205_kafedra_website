from django.urls import path
from . import views



urlpatterns = [

    path('', views.index, name='index'),
    path('esp_kafedra', views.esp_kaf, name='esp_kaf'),
    path('eng_kafedra', views.eng_kaf, name='eng_kaf'),
    path('novosti', views.novosti, name='novosti'),
]
