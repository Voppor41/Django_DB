from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import UserRegister
from django.core.paginator import Paginator


# Функция для создания общего контекста меню
def menu_context():
    return {
        'title': "Main page",
        'main': "Главная",
        'shop': "Магазин",
        'bin': "Корзина",
        'news': "Новости",
    }

# Представления
def menu(request):
    return render(request, 'fourth_task/menu.html', menu_context())

def bin_page(request):
    context = menu_context()  # Общий контекст меню
    return render(request, 'fourth_task/bin-page.html', context)

def shop_page(request):
    context = menu_context()  # Общий контекст меню
    Games = Game.objects.all()
    context.update({
        'buy': 'Купить',
        'games': Games,
    })
    return render(request, 'fourth_task/shop-page.html', context)

def main_page(request):
    return render(request, 'fourth_task/main-page.html', menu_context())

def news_page(request):
    posts = News.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    return render(request, "fourth_task/news.html", {'news': news})


def sign_up_by_django(request):
    info = {}  # Пустой словарь для передачи контекста
    if request.method == 'POST':
        form = UserRegister(request.POST)  # Передаем список пользователей в форму
        if form.is_valid():
            username = form.cleaned_data['username']
            age = form.cleaned_data['age']
            # Записываем пользователя и выполняем дополнительные действия, если необходимо
            Buyer.objects.create(
                name=username,
                age=age
            )
            return HttpResponse(f"Приветствуем, {username}!")
        else:
            # Если форма не прошла валидацию, выводим ошибки
            info['form'] = form  # Передаем форму с ошибками в шаблон
    else:
        form = UserRegister()  # Пустая форма

    info['form'] = form  # Передаем форму в шаблон
    return render(request, 'fifth_task/registration_page.html', info)