from django.urls import path
from . import views

urlpatterns = [
    path('uno_a_uno', views.index, name='uno_a_uno_index'),
    
]