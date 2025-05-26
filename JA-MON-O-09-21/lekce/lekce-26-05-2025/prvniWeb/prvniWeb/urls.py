"""
URL configuration for prvniWeb project.

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
from mojeaplikace import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('pozdrav/', views.pozdrav, name="pozdrav"),
    path('seznam/', views.seznam, name="seznam"),
    path('uzivatele/', views.uzivatele, name="uzivatele"),
    path('dynamicSeznam/', views.dynamicSeznam, name="dynamicSeznam"),
    path('osloveni/<str:jmeno>', views.osloveni, name="osloveni"),
    path('osloveni/<str:jmeno>/<int:vek>', views.test, name="TestOsloveni"),
    path("formHello/", views.formHello, name="formHello"),
]
