from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/<pk>/', views.contacts, name='contacts'), # is it ok to have same name???
]