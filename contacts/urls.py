from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_contacts, name='search'),
    path('add/', views.add_contact, name='add'),    
    path('delete/<int:pk>/', views.delete_contact, name='delete'),
    path('edit/<int:pk>/', views.edit_contact, name='edit'),
]
