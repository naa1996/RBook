from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # роут для отображения страницы
    path('formalization', views.formalization, name='formalization'),
    # роут для обновления данных
    path('updateFormalization', views.updateFormalization, name='updateFormalization'),
    # роут для поиска
    path('searchFormalization', views.searchFormalization, name='searchFormalization'),
    # роут для изменения количества
    path('quantityFormalization', views.quantityFormalization, name='quantityFormalization'),
    # роут для отображения страницы
    path('request', views.request, name='request'),
    # роут для обновления данных
    path('updateRequest', views.updateRequest, name='updateRequest'),
    # роут для поиска
    path('searchRequest', views.searchRequest, name='searchRequest'),
    # роут для отображения страницы
    path('clients', views.clients, name='clients'),
    # роут для поиска
    path('searchClients', views.searchClients, name='searchClients'),
    # роут для отображения страницы
    path('books', views.book, name='book'),
    # роут для поиска
    path('searchBooks', views.searchBooks, name='searchBooks'),
    # роут для отображения страницы
    path('', views.index, name='index'),
]