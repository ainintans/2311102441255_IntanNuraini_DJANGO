from django.shortcuts import render
from .models import Drakor

def home(request):
    return render(request, 'rekomendasi/home.html')

def daftar_drakor(request):
    semua_drakor = Drakor.objects.all()
    return render(request, 'rekomendasi/daftar_drakor.html', {'drakor_list': semua_drakor})
