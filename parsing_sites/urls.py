from django.urls import path

from . import views

app_name = 'parsing_sites'

urlpatterns = [
    path('', views.index, name='index')
    ]
