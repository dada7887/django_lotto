"""site_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from lotto import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.index), #http://127.0.0.1:8000 url에 대응된다. <-http://www.mydomain.com, 충돌방지(index 충돌)
    path('hello/',views.hello,name='hello_main'),#name=별칭! url이 복잡해질 때 대비
    path('lotto/',views.index,name='index'),
    path('lotto/new/',views.post,name='new_lotto'),
    #path('new/', views.index), #http://127.0.0.1:8000/new url에 대응된다. <-http://www.mydomain.com/new
    path('lotto/<int:lottokey>/detail/',views.detail,name='detail'),
]
