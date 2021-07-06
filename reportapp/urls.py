from django.urls import path
from reportapp import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.report, name='report'),
]
