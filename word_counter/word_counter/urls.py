"""word_counter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import word_app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', word_app.views.home, name="home"),
    path('about/', word_app.views.about, name="about"),
    path('loading/', word_app.views.loading, name="loading"),
    path('result/', word_app.views.result, name="result"),
    path('result2/', word_app.views.result2, name="result2"),
]
