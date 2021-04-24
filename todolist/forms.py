from django import forms
# from models import Expenditure
from django.core import validators
from . import models, views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TodoForm(forms.Form):
    name = forms.CharField(label='Имя', validators=[validators.RegexValidator()])
    authors = forms.CharField(label='Автор')
    cost = forms.FloatField(label='Стоимость')
    publishing_house = forms.CharField(label='Издательство')
    year_of_publishing = forms.IntegerField(label='Год издания')
    number_of_pages = forms.IntegerField(label='Количество страниц')
    number_of_copies = forms.IntegerField(label='Количество экзмепляров')
    udc = forms.CharField(label='УДК')
    bbk = forms.CharField(label='ББК')
    keywords = forms.CharField(label='Ключевые слова')
    short_description = forms.CharField(label='Краткое описание')


class TodoFormCl(forms.Form):
    surname = forms.CharField(label='Фамилия')
    name = forms.CharField(label='Имя')
    residence_address = forms.CharField(label='Адрес поживания')
    telephone = forms.CharField(label='Телефон')


class TodoFormAS(forms.Form):
    application_status = forms.CharField()


class TodoFormR(forms.Form):
    name = forms.CharField(label='Название')
    authors = forms.CharField(label='Автор')
    client = forms.ModelChoiceField(models.Clients.objects.all(), label='Клиент')
    application_status = forms.ModelChoiceField(models.ApplicationStatus.objects.all(), label='Состояние заявки')
    keywords = forms.CharField(label='Ключевые слова')
    publishing_house = forms.CharField(label='Издательство')
    the_year_of_publishing = forms.IntegerField(label='Год издания')
    number_of_pages = forms.IntegerField(label='Количество страниц')
    number_of_copies = forms.IntegerField(label='Количество экзмепляров')
    date = forms.DateTimeInput(attrs={'type': 'datetime-local'})


class TodoFormF(forms.Form):
    books = forms.ModelChoiceField(models.Books.objects.all(), label='Название')
    quantity = forms.IntegerField(label='Количество')
    # cost = forms.FloatField(label='Стоимость')
    # total_cost = forms.FloatField(label='Итоговая стоимость')
    # cost = forms.FloatField(widget = forms.TextInput(attrs={'readonly':'readonly'}), label='Стоимость')
    # total_cost = forms.FloatField(widget = forms.TextInput(attrs={'readonly':'readonly'}), label='Итоговая стоимость')
    client = forms.ModelChoiceField(models.Clients.objects.all(), label='Клиент')
    employee = forms.ModelChoiceField(models.Employee.objects.all(), label='Сотрудник')
    status = forms.ModelChoiceField(models.ClearanceStatus.objects.all(), label='Статус')
    date = forms.DateTimeInput(attrs={'type': 'datetime-local'})
    # widgets = {
    #     'dateL': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    # }


class TodoFormE(forms.Form):
    surname = forms.CharField(label='Фамилия')
    name = forms.CharField(label='Имя')
    telephone = forms.CharField(label='Телефон')
    residence_address = forms.CharField(label='Адрес')


class UserRegistration(UserCreationForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторный пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


def clean_password2(self):
    cd = self.cleaned_data
    if cd['password'] != cd['password']:
        raise forms.ValidationError('Пароли не совпадают')
    return cd['password']


# class TodoFormSt(forms.Form):
#     status = forms.ModelChoiceField(models.ClearanceStatus.objects.all())

    # class Meta:
    #     fields = ('status')
