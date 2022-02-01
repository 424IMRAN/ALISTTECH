from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name='home'),
    path(r'about', views.about, name='about'),
    path(r'contact', views.contact, name='contact'),
]