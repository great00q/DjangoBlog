"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Article import views

urlpatterns = [
    url(r'^article/(?P<id>\d+).html$',views.Articles,name='article'),
    url(r'^cate/(?P<id>\d+)\.html$',views.Cates,name='cate'),
    url(r'^tags/(?P<id>\d+).html$',views.Tags,name='tag'),
    url(r'^comment/(?P<id>\d+)$',views.Comments,name='comment'),
    url(r'',views.Index)
]
