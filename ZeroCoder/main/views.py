from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render

def layoute(request):
    context = {
        'page_title': 'Главная страница',
        'page_text': 'Это пример текстового блока для данной страницы.',
        'sidebar_image': '/static/main/img/target.png',
        'first_image': '/static/main/img/watch-gold.jpg',
        'second_image': '/static/main/img/money-man.png',
    }
    return render(request, 'main/layoute.html', context)
def index(request):
    return render(request, 'main/index.html')
def cash_in(request):
    return render(request, 'main/cash_in.html')
def cash_on(request):
    return render(request, 'main/cash_on.html')
def save(request):
    return render(request, 'main/save.html')
def new(request):
    return render(request, 'main/new.html')
def data(request):
    return HttpResponse("<h1>Отсюда можно будет получить доступ к базам данных моего первого проекта на Django</h1>")

def test(request):
    return HttpResponse("<h1>Ну а это тестовая страничка моего первого проекта на Django</h1>")