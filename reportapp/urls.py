from django.urls import path
from reportapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('testbed', views.testbed, name='testbed'),
    #path('', views.report, name='report'),
]
