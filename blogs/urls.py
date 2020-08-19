from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from blogs import views 
urlpatterns=[
        url(r'foods.*',views.foods, name='foods'),
        url(r'drinks.*',views.drinks, name='drinks'),
]

