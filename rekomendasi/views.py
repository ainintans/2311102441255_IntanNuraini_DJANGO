from django.shortcuts import render, get_object_or_404
from .models import Drama

def home(request):
    dramas = Drama.objects.all()
    return render(request, 'home.html', {'dramas': dramas})

def drama_detail(request, drama_id):
    drama = get_object_or_404(Drama, id=drama_id)
    return render(request, 'drama_detail.html', {'drama': drama})
