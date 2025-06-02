"""
URL configuration for moje_aplikace project.

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
from django.contrib import admin
from django.urls import path
from zamestnanci import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('dept_edit/<int:deptno>/', views.dept_edit, name='dept_edit'),
    path('dept_detail/<int:deptno>/', views.dept_detail, name='dept_detail'),
    path('dept_delete/<int:deptno>/', views.dept_delete, name='dept_delete'),
    path('dept_add/', views.dept_add, name='dept_add'),
]
