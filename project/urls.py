from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('performance/', views.performance, name='performance'),
    path('about/', views.about , name='about'),
    path('contact/', views.contact , name='contact'),
    path('abstarct/', views.abstract , name='abstract'),
    path('upload/', views.upload , name='upload'),
    path('result/', views.result , name='result'),

]
