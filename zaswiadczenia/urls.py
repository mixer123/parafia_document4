from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import  static
from django.conf import settings
from django.views.generic import TemplateView

from zaswiadczenia import views

urlpatterns = [
    path('a4/', views.document_a4, name='a4'),
    ]