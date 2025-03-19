from django.urls import path
from .views import list_drakor

urlpatterns = [
    path('', list_drakor, name='list_drakor'),
]
