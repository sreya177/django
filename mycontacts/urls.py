from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from mycontacts import views
urlpatterns = [
        url(r'mine.*',views.mine, name='mine'),
        url(r'friend.*',views.friend, name='friend'),
        ]
