from django import forms
from django.core import validators
from . import models

class TodoForm(forms.Form):
    name = forms.CharField(validators=[validators.RegexValidator()])
    authors = forms.CharField()
    cost = forms.FloatField()
    publishing_house = forms.CharField()
    year_of_publishing = forms.IntegerField()
    number_of_pages = forms.IntegerField()
    number_of_copies = forms.IntegerField()
    udc = forms.CharField()
    bbk = forms.CharField()
    keywords = forms.CharField()
    short_description = forms.CharField()

class TodoFormCl(forms.Form):
    surname = forms.CharField()
    name = forms.CharField()
    residence_address = forms.CharField()
    telephone = forms.CharField()

class TodoFormAS(forms.Form):
    application_status = forms.CharField()

class TodoFormR(forms.Form):
    name = forms.CharField()
    authors = forms.CharField()
    client = forms.ModelChoiceField(models.Clients.objects.all())
    application_status = forms.ModelChoiceField(models.ApplicationStatus.objects.all())
    keywords = forms.CharField()
    publishing_house = forms.CharField()
    the_year_of_publishing = forms.IntegerField()
    number_of_pages = forms.IntegerField()
    number_of_copies = forms.IntegerField()

class TodoFormF(forms.Form):
    books = forms.ModelChoiceField(models.Books.objects.all())
    quantity = forms.IntegerField()
    client = forms.ModelChoiceField(models.Clients.objects.all())
    employee = forms.ModelChoiceField(models.Employee.objects.all())
    status = forms.ModelChoiceField(models.ClearanceStatus.objects.all())