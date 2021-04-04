from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('formalization', views.formalization, name='formalization'),
    path('request', views.request, name='request'),
    path('clients', views.clients, name='clients'),
    path('books', views.book, name='book'),
    path('', views.index, name='index'),
]