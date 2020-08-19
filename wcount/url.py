from django.contrib import admin
from django.urls import path
from wcount import views
urlpatterns=[
        path('admin/',admin.site.urls),
        path('myhome/',views.home,name='home'),
        path('aboutus/',views.aboutus,name='aboutus'),
        ]
