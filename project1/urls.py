"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app1.views import *
from comments.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', register),
    path('succsesful/', reg_succsesful, name = 'succsesful'),
    path('auth/', auth_page, name = 'auth_page'),
    path('welcome/', welcome, name = 'welcome'),
    path('logout/', user_logout, name = 'user_logout'),
    path('comments/', showpage, name = 'show_comments'),
]
