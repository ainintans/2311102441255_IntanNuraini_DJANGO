from django.shortcuts import render, get_object_or_404, redirect
from .models import Drakor
from django.db.models import Q

def home(request):
    drakor_terbaru = Drakor.objects.all().order_by('-id')[:3]
    return render(request, 'rekomendasi/home.html', {'drakor_terbaru': drakor_terbaru})

def daftar_drakor(request):
    query = request.GET.get('q', '')
    if query:
        drakor_list = Drakor.objects.filter(
            Q(genre__icontains=query) |
            Q(judul__icontains=query) |
            Q(sinopsis__icontains=query)
        )
    else:
        drakor_list = Drakor.objects.all()

    
    favorit_ids = request.session.get('favorit_ids', [])

    return render(request, 'rekomendasi/daftar_drakor.html', {
        'drakor_list': drakor_list,
        'query': query,
        'favorit_ids': favorit_ids
    })

def detail_drakor(request, id):
    drakor = get_object_or_404(Drakor, id=id)

    
    favorit_ids = request.session.get('favorit_ids', [])
    is_favorit = id in favorit_ids

    return render(request, 'rekomendasi/detail_drakor.html', {
        'drakor': drakor,
        'is_favorit': is_favorit
    })

def toggle_favorit(request, drakor_id):
    favorit_ids = request.session.get('favorit_ids', [])

    if drakor_id in favorit_ids:
        favorit_ids.remove(drakor_id)
    else:
        favorit_ids.append(drakor_id)

    request.session['favorit_ids'] = favorit_ids
    return redirect('detail_drakor', id=drakor_id)

def favorit_saya(request):
    favorit_ids = request.session.get('favorit_ids', [])
    drakor_favorit = Drakor.objects.filter(id__in=favorit_ids)

    return render(request, 'rekomendasi/favorit.html', {
        'drakor_list': drakor_favorit
    })
