from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('drama/<int:drama_id>/', views.drama_detail, name='drama_detail'),
]
