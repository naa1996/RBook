from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # роут для регистрации
    path('register/', views.register, name='register'),
    # роут для добавлния данных о сотруднике
    # path(r'^register/userRegister/$', views.userRegister, name='userRegister'),
    path('register/userRegister', views.userRegister, name='userRegister'),
    #роут для добавления сотрудника
    # path(r'^register/createRegister/$', views.createRegister, name='createRegister'),
    path('register/createRegister', views.createRegister, name='createRegister'),
    # роут для аутентификации
    path(r'^accounts/login/$', views.login),
    # роут для выхода
    path(r'^accounts/logout/$', views.logout),
    # роут для отображения страницы
    path('formalization', views.formalization, name='formalization'),
    # роут для обновления данных
    path('updateFormalization', views.updateFormalization, name='updateFormalization'),
    # роут для поиска
    path('searchFormalization', views.searchFormalization, name='searchFormalization'),
    # роут для изменения количества
    path('quantityFormalization', views.quantityFormalization, name='quantityFormalization'),
    # роут для удаления
    path('deleteFormalization', views.deleteFormalization, name='deleteFormalization'),
    # роут для отображения страницы
    path('request', views.request, name='request'),
    # роут для обновления данных
    path('updateRequest', views.updateRequest, name='updateRequest'),
    # роут для поиска
    path('searchRequest', views.searchRequest, name='searchRequest'),
    # роут для удаления
    path('deleteRequest', views.deleteRequest, name='deleteRequest'),
    # роут для отображения страницы
    path('clients', views.clients, name='clients'),
    # роут для поиска
    path('searchClients', views.searchClients, name='searchClients'),
    # роут для удаления
    path('deleteClient', views.deleteClient, name='deleteClient'),
    # роут для отображения страницы
    path('books', views.book, name='book'),
    # роут для поиска
    path('searchBooks', views.searchBooks, name='searchBooks'),
    # роут для удаления
    path('deleteBooks', views.deleteBooks, name='deleteBooks'),
    # роут для отображения страницы
    path('', views.index, name='index'),
]