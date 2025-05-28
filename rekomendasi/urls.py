from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('drakor/', views.daftar_drakor, name='daftar_drakor'),
]
