from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('data', views.data),
    path('cash_in', views.cash_in, name='cash_in'),
    path('cash_on', views.cash_on, name='cash_on'),
    path('save', views.save, name='save'),
    path('test', views.test)
]


