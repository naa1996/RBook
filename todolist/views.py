from django.shortcuts import render
from . import models, forms


def index(request):
    q = models.Books.objects.all()
    if request.method == "POST":
        form = forms.TodoForm(request.POST)
        if form.is_valid():
            models.Books.objects.create(
                name=form.cleaned_data['name'],
                authors=form.cleaned_data['authors'],
                cost=form.cleaned_data['cost'],
                publishing_house=form.cleaned_data['publishing_house'],
                year_of_publishing=form.cleaned_data['year_of_publishing'],
                number_of_pages=form.cleaned_data['number_of_pages'],
                number_of_copies=form.cleaned_data['number_of_copies'],
                udc=form.cleaned_data['udc'],
                bbk=form.cleaned_data['bbk'],
                keywords=form.cleaned_data['keywords'],
                short_description=form.cleaned_data['short_description'],
                # is_end=False
            )
    else:
        form = forms.TodoForm()
    return render(request, 'index.html', {
        'title': 'Главная страница',
        'List_todo': q,
        'create_form': form
    })


def book(request):
    s = models.Books.objects.all()
    if request.method == "POST":
        form = forms.TodoForm(request.POST)
        if form.is_valid():
            models.Books.objects.create(
                name=form.cleaned_data['name'],
                authors=form.cleaned_data['authors'],
                cost=form.cleaned_data['cost'],
                publishing_house=form.cleaned_data['publishing_house'],
                year_of_publishing=form.cleaned_data['year_of_publishing'],
                number_of_pages=form.cleaned_data['number_of_pages'],
                number_of_copies=form.cleaned_data['number_of_copies'],
                udc=form.cleaned_data['udc'],
                bbk=form.cleaned_data['bbk'],
                keywords=form.cleaned_data['keywords'],
                short_description=form.cleaned_data['short_description'],
                # is_end=False
            )
    else:
        form = forms.TodoForm()
    return render(request, 'book.html', {
            'title': 'Книги',
            'List_todo': s,
            'create_form': form
    })


def clients(request):
    a = models.Clients.objects.all()
    if request.method == "POST":
        form = forms.TodoFormCl(request.POST)
        if form.is_valid():
            models.Clients.objects.create(

                surname=form.cleaned_data['surname'],
                name=form.cleaned_data['surname'],
                residence_address=form.cleaned_data['residence_address'],
                telephone=form.cleaned_data['telephone'],
            )
    else:
        form = forms.TodoFormCl()
    return render(request, 'clients.html', {
            'title': 'Клиенты',
            'List_todo1': a,
            'create_form1': form
    })


def request(request):
    d = models.Request.objects.all()
    if request.method == "POST":
        form = forms.TodoFormR(request.POST)
        if form.is_valid():
            models.Request.objects.create(
                name=form.cleaned_data['name'],
                authors=form.cleaned_data['authors'],
                client=form.cleaned_data['client'],
                application_status=form.cleaned_data['application_status'],
                keywords=form.cleaned_data['keywords'],
                publishing_house=form.cleaned_data['publishing_house'],
                the_year_of_publishing=form.cleaned_data['the_year_of_publishing'],
                number_of_pages=form.cleaned_data['number_of_pages'],
                number_of_copies=form.cleaned_data['number_of_copies'],
            )
    else:
        form = forms.TodoFormR()
    return render(request, 'request.html', {
            'title': 'Заявки',
            'List_todo2': d,
            'create_form2': form
    })


def formalization(request):
    w = models.Formalization.objects.all()
    if request.method == "POST":
        form = forms.TodoFormF(request.POST)
        if form.is_valid():
            models.Formalization.objects.create(
                books=form.cleaned_data['books'],
                quantity=form.cleaned_data['quantity'],
                client=form.cleaned_data['client'],
                employee=form.cleaned_data['employee'],
                status=form.cleaned_data['status'],
            )
    else:
        form = forms.TodoFormF()
    return render(request, 'formalization.html', {
            'title': 'Заявки',
            'List_todo3': w,
            'create_form3': form
    })
