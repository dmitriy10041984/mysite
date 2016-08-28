from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),

]