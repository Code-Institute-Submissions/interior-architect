from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<pk>/', views.add, name='add'),
    path('remove/<pk>/', views.remove, name='remove'),
    path('charge', views.charge, name='charge'),
    path('success', views.success, name='success'),
]
