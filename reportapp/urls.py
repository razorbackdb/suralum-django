from django.urls import path
from reportapp import views
from wkhtmltopdf.views import PDFTemplateView

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.report, name='report'),
]
