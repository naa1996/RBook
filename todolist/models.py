from django.db import models
from django.forms import ModelForm


class ApplicationStatus(models.Model):
    """
    Состояние заявки
    """
    application_status = models.CharField(max_length=50, verbose_name='Наименование')
    """is_end = models.BooleanField()"""
    def __str__(self):
        return self.application_status


class Clients(models.Model):
    """
    Клиенты
    """
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=10, verbose_name='Имя')
    residence_address = models.CharField(max_length=50, verbose_name='Адрес проживания')
    telephone = models.CharField(max_length=12, verbose_name='Телефон')

    def __str__(self):
        return self.surname
        # return self.clients


class Request(models.Model):
    """
    Заявка
    """
    name = models.CharField(max_length=100, verbose_name='Название книги')
    authors = models.CharField(max_length=50, verbose_name='Автор')
    client = models.ForeignKey('Clients', on_delete=models.DO_NOTHING, verbose_name='Клиент')
    application_status = models.ForeignKey('ApplicationStatus', on_delete=models.DO_NOTHING, verbose_name='Состояние заявки')
    keywords = models.CharField(max_length=500, verbose_name='Ключевые слова')
    publishing_house = models.CharField(max_length=100, verbose_name='Издательство')
    the_year_of_publishing = models.IntegerField(verbose_name='Год издания')
    number_of_pages = models.IntegerField(verbose_name='Количество страниц')
    number_of_copies = models.IntegerField(verbose_name='Количество экзмепляров')


class Books(models.Model):
    """
    Книги
    """
    name = models.CharField(max_length=100, verbose_name='Название')
    authors = models.CharField(max_length=100, verbose_name='Авторы')
    cost = models.FloatField(verbose_name='Стоимость')
    publishing_house = models.CharField(max_length=100, verbose_name='Издательство')
    year_of_publishing = models.IntegerField(verbose_name='Год издания')
    number_of_pages = models.IntegerField(verbose_name='Количество страниц')
    number_of_copies = models.IntegerField(verbose_name='Количество экзмепляров')
    udc = models.CharField(max_length=50, verbose_name='УДК')
    bbk = models.CharField(max_length=50, verbose_name='ББК')
    keywords = models.CharField(max_length=50, verbose_name='Ключевые слова')
    short_description = models.TextField(verbose_name='Краткое описание')

    def __str__(self):
        return self.name


class ClearanceStatus(models.Model):
    """
    Статус оформления книги
    """
    status_name = models.CharField(max_length=50, verbose_name='Наименование')

    def __str__(self):
        return self.status_name


class Employee(models.Model):
    """
    Сотрудники
    """
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=10, verbose_name='Имя')
    telephone = models.CharField(max_length=12, verbose_name='Телефон')
    residence_address = models.CharField(max_length=50, verbose_name='Адрес')

    def __str__(self):
        return self.surname


class Formalization(models.Model):
    """
    Оформление книги
    """
    books = models.ForeignKey('Books', on_delete=models.DO_NOTHING, verbose_name='Название книги')
    quantity = models.IntegerField(verbose_name='Количество')
    client = models.ForeignKey('Clients', on_delete=models.DO_NOTHING, verbose_name='Клиент')
    employee = models.ForeignKey('Employee', on_delete=models.DO_NOTHING, verbose_name='Сотрудник')
    status = models.ForeignKey('ClearanceStatus', on_delete=models.DO_NOTHING, verbose_name='Статус')

    # class Meta:
    #     managed=False
    #     db_table='table'