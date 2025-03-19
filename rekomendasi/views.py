from django.shortcuts import render
from .models import Drakor

def list_drakor(request):
    drakor_list = Drakor.objects.all()
    return render(request, 'rekomendasi/list.html', {'drakor_list': drakor_list})
