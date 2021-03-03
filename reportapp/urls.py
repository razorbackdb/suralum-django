from django.urls import path
from reportapp import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.report, name='report'),
]
