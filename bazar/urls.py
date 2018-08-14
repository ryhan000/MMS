from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:bazar_id>/', views.item, name='item'),
    path('create/', views.bazar, name='bazar'),
    path('<slug:name>/', views.bazar_indi, name='bazar_indi'),
   
]