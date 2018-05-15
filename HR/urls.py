"""RMSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # path('', views.HR_Info),
    path('',       views.PersonListView.as_view(), name="list"),
    path('OK',      TemplateView.as_view(template_name="HR/success.html")  , name="success"),
    path('<int:pk>', views.personViews.as_view(),    name="detail"),
    path('person/add/', views.personAdd.as_view(),    name="personAdd"),
    path('person/<int:pk>/', views.personUpdate.as_view(),    name="personUpdate"),
    path('person/<int:pk>/del', views.personDelete.as_view,    name="personDel"),
    
]
