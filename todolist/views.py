from django.shortcuts import render
from . import models, forms
from django.views import View
import datetime
from django.shortcuts import redirect
from .models import Formalization, Request, Clients, Books, User
from .forms import UserRegistration
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render
from django.db.models import F


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


def deleteBooks(request):
    w = models.Books.objects.get(id = int(request.POST['id_del']))
    form = forms.TodoForm(request.POST)
    ss = Books._meta._get_fields()
    # print('ss', ss)
    if request.method == 'POST':
        models.Books.objects.filter(id = int(request.POST['id_del'])).delete()
        # w =models.Formalization.objects.get(id = int(request.POST['id_del']))

    w = models.Books.objects.all()
    return redirect('book')


def searchBooks(request):
    form = forms.TodoForm()
    if request.GET.keys():
        if request.GET.get('searchB') != ' ':
            keyword = str(request.GET.get('searchB')).lower().strip()
            mod = Books.objects.filter(Q(name__icontains=keyword) | Q(name__startswith=keyword) | Q(authors__contains=keyword) | Q(authors__startswith=keyword) | Q(cost__contains=keyword) | Q(cost__startswith=keyword) | Q(publishing_house__contains=keyword) | Q(publishing_house__startswith=keyword) | Q(year_of_publishing__contains=keyword) | Q(year_of_publishing__startswith=keyword) | Q(number_of_pages__contains=keyword) | Q(number_of_pages__startswith=keyword) | Q(number_of_copies__contains=keyword) | Q(number_of_copies__startswith=keyword) | Q(udc__contains=keyword) | Q(udc__startswith=keyword) | Q(bbk__contains=keyword) | Q(bbk__startswith=keyword) | Q(keywords__contains=keyword) | Q(keywords__startswith=keyword) | Q(short_description__contains=keyword) | Q(short_description__startswith=keyword)).all()
            return render(request, 'book.html', {
                'title': 'Книги',
                'create_form': form,
                'List_todo': mod,
            })
        else:
            return redirect('book')  #
    else:
        return redirect('book')  #


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
            )
    else:
        form = forms.TodoForm()
    return render(request, 'book.html', {
            'title': 'Книги',
            'List_todo': s,
            'create_form': form
    })


def deleteClient(request):
    w = models.Clients.objects.get(id = int(request.POST['id_del']))
    form = forms.TodoFormCl(request.POST)
    ss = Clients._meta._get_fields()
    print('ss', ss)
    if request.method == 'POST':
        models.Clients.objects.filter(id = int(request.POST['id_del'])).delete()
        # w =models.Formalization.objects.get(id = int(request.POST['id_del']))

    w = models.Clients.objects.all()
    return redirect('clients')


def searchClients(request):
    # mod = Formalization.objects.all()
    form = forms.TodoFormCl()
    if request.GET.keys():
        # print('dGGG11111')
        if request.GET.get('searchCl') != ' ':
            # print('dGGG22222')
            keyword = str(request.GET.get('searchCl')).lower().strip()
            mod = Clients.objects.filter(Q(surname__icontains=keyword) | Q(surname__startswith=keyword) | Q(name__contains=keyword) | Q(name__startswith=keyword) | Q(residence_address__contains=keyword) | Q(residence_address__startswith=keyword) | Q(telephone__contains=keyword) | Q(telephone__startswith=keyword)).all()
            # print(mod)
            return render(request, 'clients.html', {
                'title': 'Клиенты',
                'create_form1': form,
                'List_todo1': mod,
            })
            # print('111111')
        else:
            return redirect('clients')  #
    else:
        return redirect('clients')  #


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


def deleteRequest(request):
    w = models.Request.objects.get(id = int(request.POST['id_del']))
    form = forms.TodoFormR(request.POST)
    ss = Request._meta._get_fields()
    print('ss', ss)
    if request.method == 'POST':
        models.Request.objects.filter(id = int(request.POST['id_del'])).delete()
        # w =models.Request.objects.get(id = int(request.POST['id_del']))

    w = models.Request.objects.all()
    return redirect('request')


def updateRequest(request): # вот это метод для обновления данных
    # 1. получаем какой-то реквест (в реквесте необходим id)
    # 2. делаем запрос в базу данных, и получаем строку по id
    # 3. выполняем изменения этой базы данных, относительно реквеста
    # 4. сохраняем данные
    w = models.Request.objects.get(id= int(request.POST['id_post']))
    form = forms.TodoFormR(request.POST)
    application_status_id = 1

    if request.method == 'POST':
        if (int(request.POST['status2']) == 1):
            application_status_id = 1
        else:
            application_status_id = 2
        data = request.POST
        models.Request.objects.filter(id = int(request.POST['id_post'])).update(application_status = application_status_id)
        w = models.Request.objects.get(id=int(request.POST['id_post']))

    w = models.Request.objects.all()
    return redirect('request')


def searchRequest(request):
    form = forms.TodoFormR()
    if request.GET.keys():
        if request.GET.get('searchR') != ' ':
            keyword = str(request.GET.get('searchR')).lower().strip()
            mod = Request.objects.filter(Q(name__icontains=keyword) | Q(name__startswith=keyword) | Q(authors__contains=keyword) | Q(authors__startswith=keyword) | Q(client__surname__contains=keyword) | Q(client__surname__startswith=keyword) | Q(application_status__application_status__contains=keyword) | Q(application_status__application_status__startswith=keyword) | Q(keywords__contains=keyword) | Q(keywords__startswith=keyword) | Q(publishing_house__contains=keyword) | Q(publishing_house__startswith=keyword) | Q(the_year_of_publishing__contains=keyword) | Q(the_year_of_publishing__startswith=keyword)| Q(number_of_pages__contains=keyword) | Q(number_of_pages__startswith=keyword)| Q(number_of_copies__contains=keyword) | Q(number_of_copies__startswith=keyword)| Q(date__contains=keyword) | Q(date__startswith=keyword)).all()
            return render(request, 'request.html', {
                'title': 'Заявки',
                'create_form2': form,
                'List_todo2': mod,
            })
        else:
            return redirect('request')
    else:
        return redirect('request')


def request(request):
    d = models.Request.objects.all()
    if request.method == "POST":
        date_in = request.POST['dateR']
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
                date=formatDateForPython(date_in)
            )
    else:
        form = forms.TodoFormR()
    return render(request, 'request.html', {
            'title': 'Заявки',
            'List_todo2': d,
            'create_form2': form
    })


def deleteFormalization(request):
    w = models.Formalization.objects.get(id = int(request.POST['id_del']))
    form = forms.TodoFormF(request.POST)
    ss = Formalization._meta._get_fields()
    # print('ss', ss)
    if request.method == 'POST':
        models.Formalization.objects.filter(id = int(request.POST['id_del'])).delete()
        # w =models.Formalization.objects.get(id = int(request.POST['id_del']))

    w = models.Formalization.objects.all()
    return redirect('formalization')


def updateFormalization(request): # вот это метод для обновления данных
    # 1. получаем какой-то реквест (в реквесте необходим id)
    # 2. делаем запрос в базу данных, и получаем строку по id
    # 3. выполняем изменения этой базы данных, относительно реквеста
    # 4. сохраняем данные
    w = models.Formalization.objects.get(id= int(request.POST['id_post']))
    form = forms.TodoFormF(request.POST)
    status_id = 1

    if request.method == 'POST':
        if (int(request.POST['status1']) == 1):
            status_id = 1
        else:
            status_id = 2
        data = request.POST
        models.Formalization.objects.filter(id = int(request.POST['id_post'])).update(status = status_id)
        w = models.Formalization.objects.get(id=int(request.POST['id_post']))

    w = models.Formalization.objects.all()
    return redirect('formalization')# вот это предыдущая страница


def searchFormalization(request):
    form = forms.TodoFormF()
    if request.GET.keys():
        if request.GET.get('searchF') != ' ':
            keyword = str(request.GET.get('searchF')).lower().strip()
            mod = Formalization.objects.filter(Q(books__name__icontains=keyword) | Q(books__name__startswith=keyword) | Q(quantity__contains=keyword) | Q(quantity__startswith=keyword) | Q(client__surname__contains=keyword) | Q(client__surname__startswith=keyword) | Q(employee__surname__contains=keyword) | Q(employee__surname__startswith=keyword) | Q(status__status_name__contains=keyword) | Q(status__status_name__startswith=keyword) | Q(date__contains=keyword) | Q(date__startswith=keyword)).all()
            # mod = Formalization.objects.all()
            return render(request, 'formalization.html', {
                'title': 'Оформление',
                'create_form3': form,
                'List_todo3': mod,
            })
        else:
            return redirect('formalization')
    else:
        return redirect('formalization')


def quantityFormalization(request):
    # 1Создать метод для покупки
    # 2Этот метод имеет параметр response
    # 3 Респонс - объект в котором хранятся два параметра(свойства): id_книги и количество книг
    # 4 по id книги я нахожу книгу в БД
    # 5 я из книги которую нашел по id вытягиваю значение "количество" книг,
    # которые находятся в БД, затме я обновляю количество книг,
    # Т,Е, беру общее количество книг в магазин _ кол книг которые купили
    w = models.Formalization.objects.all()
    idd = request.POST['books']
    quantity1 = float(request.POST['quantity'])
    client = request.POST['client']
    employee = request.POST['employee']
    status = request.POST['status']
    date_in = request.POST['dateF']
    if request.method == 'POST':
        f = Books.objects.filter(id=idd).first()
        ff = forms.TodoFormF(request.POST)
        if f is not None and ff.is_valid():
                if (f.number_of_copies != 0) and (f.number_of_copies > 0) and (f.number_of_copies != [-1]):
                    if quantity1 <= f.number_of_copies:
                        ss = Books._meta._get_fields()
                        ss1 = Formalization._meta._get_fields()
                        #количество экземпляров
                        f.number_of_copies -= int(quantity1)
                        #стоимость
                        cost = f.cost
                        total_cost = cost * quantity1
                        f.save()
                        models.Formalization.objects.create(
                            books=ff.cleaned_data['books'],
                            quantity=ff.cleaned_data['quantity'],
                            cost=cost,
                            total_cost=total_cost,
                            client=ff.cleaned_data['client'],
                            employee=ff.cleaned_data['employee'],
                            status=ff.cleaned_data['status'],
                            date=formatDateForPython(date_in)
                        )
                        # print('dsd', ff)
                        # w = models.Request.objects.get(id=int(request.POST['id_post']))
                        w = models.Formalization.objects.all()
                        # createFormalization(request)

                        return redirect('formalization')
                    else:
                        messages.error(request, 'Превышение количества имеющихся книг', extra_tags='safe')
                        return redirect('formalization')
                else:
                    messages.error(request, 'Книги нет в наличии', extra_tags='safe')
                    return redirect('formalization')
        else:
            messages.error(request, 'Книги нет в наличии', extra_tags='safe')
            return redirect('formalization')

    return redirect('formalization')


def createFormalization(request):
    date_in = request.POST['dateF']
    form = forms.TodoFormF(request.POST)
    if form.is_valid():
        # if request.GET.get('searchF') != '':
        #     print(1, searchF)
        models.Formalization.objects.create(
            books=form.cleaned_data['books'],
            quantity=form.cleaned_data['quantity'],
            cost=form.cleaned_data['cost'],
            total_cost=form.cleaned_data['total_cost'],
            client=form.cleaned_data['client'],
            employee=form.cleaned_data['employee'],
            status=form.cleaned_data['status'],
            date=formatDateForPython(date_in)
        )
    return redirect('formalization')

from django.shortcuts import get_list_or_404
def formalization(request):
    # вот это метод отображения страницы
    # ни в коем случае здесь не применяй изменение, создание или удаление данных, только отображение страницы
    w = models.Formalization.objects.all()
    form = forms.TodoFormF()
    return render(request, 'formalization.html', {
            'title': 'Оформление',
            'create_form3': form,
            'List_todo3': w,
    })


def formatDateForPython(date_in):
    date_processing = date_in.replace('T', '-').replace(':', '-').split('-')
    date_processing = [int(v) for v in date_processing]
    date_out = datetime.datetime(*date_processing)
    return str(date_out)


def login(request):
    return render(request, 'registration/login.html', {'title': 'Авторизация'})


def logout(request):
    return render(request, 'registration/logged_out.html', {'title': 'Выход'})
    # redirect(request, 'index.html')


def userRegister(request):
    #для добавления данных о сотруднике
    form = forms.TodoFormE(request.POST)
    surname1 = request.POST['surname']
    name1 = request.POST['name']
    telephone1 = request.POST['telephone']
    residence_address = request.POST['residence_address']
    if form.is_valid():
        ss = models.Employee.objects.filter(surname=surname1).first()
        ss1 = models.Employee.objects.filter(name=name1).first()
        st = models.Employee.objects.filter(telephone=telephone1).first()
        if not st:
            if not (ss and ss1):
                models.Employee.objects.create(
                    surname=form.cleaned_data['surname'],
                    name=form.cleaned_data['name'],
                    telephone=form.cleaned_data['telephone'],
                    residence_address=form.cleaned_data['residence_address'],
                )
                messages.error(request, 'Данные о сотуднике успешно добавлены', extra_tags='safe')
                return redirect('register')
            else:
                messages.error(request, 'Информация не добавлена. Сотрудник с таким именем уже занесен', extra_tags='safe')
                return redirect('register')
        else:
            messages.error(request, 'Информация не добавлена. Сотрудник с таким номером уже занесен', extra_tags='safe')
            return redirect('register')
    return redirect('register')



def createRegister(request):
    #для добавления сотрудника
    if request.method == 'POST':
        user_form = forms.UserRegistration(request.POST)
        users_form = forms.TodoFormE()
        password2 = request.POST['password2']
        password0 = request.POST['password1']
        username1 = request.POST['username']
        email1 = request.POST['email']
        # ss1 = models.User._meta._get_fields()
        # # f = Books.objects.filter(id=idd).first()
        ss = User.objects.filter(email=email1).first()
        ss2 = User.objects.filter(username=username1).filter()
        if not ss2:
            if not ss:
                if password0 == password2:
                    print('3')
                    # Create a new user object but avoid saving it yet
                    new_user = user_form.save(commit=False)
                    # Set the chosen password
                    new_user.set_password(user_form.cleaned_data['password1'])
                    # Save the User object
                    new_user.save()
                    messages.error(request, 'Успешно зарестрирован', extra_tags='safe')
                    return redirect('register')
                else:
                    messages.error(request, 'Не зарегестрирован. Пароли не совпадают', extra_tags='safe')
                    return redirect('register')
            else:
                messages.error(request, 'Не зарегестрирован. Пользователь с таким email уже существует', extra_tags='safe')
                return redirect('register')
        else:
            messages.error(request, 'Не зарегестрирован. Пользователь с таким логином уже существует', extra_tags='safe')
            return redirect('register')


def register(request):
    # вот это метод отображения страницы
    # ни в коем случае здесь не применяй изменение, создание или удаление данных, только отображение страницы
    # form = forms.TodoFormE()
    # form2 = forms.UserRegistration()
    user_form = forms.UserRegistration()
    users_form = forms.TodoFormE()
    return render(request, 'registration/register.html', {
            'title': 'Регистрация',
            'users_form': users_form,
            'user_form': user_form,
    })
