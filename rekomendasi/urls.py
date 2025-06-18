from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('drakor/', views.daftar_drakor, name='daftar_drakor'),
    path('drakor/<int:id>/', views.detail_drakor, name='detail_drakor'),
    path('favoritkan/<int:drakor_id>/', views.toggle_favorit, name='toggle_favorit'),
    path('favorit-saya/', views.favorit_saya, name='favorit_saya'),  # opsional
]
