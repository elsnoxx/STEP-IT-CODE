"""
URL configuration for todo_projekt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# todo_projekt/urls.py
from django.contrib import admin
from django.urls import path
from todo_app import views

app_name = 'todo_app'
urlpatterns = [
    path('admin/', admin.site.urls), # admin rozhraní
    path('', views.index, name="index"), # /
    path('done/', views.index, name='index'), # done/1
    path('delete/<innt:pk>/', views.delete, name="delete"), # delete/1
    path('edit/<int:pk>/', views.edit, name="edit"), # edit/1
    path('history/', views.history, name="history"), # history/
]
