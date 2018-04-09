from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.gato, name='gato'),
    path('saludo/', views.saludo, name = 'gato'),
]
