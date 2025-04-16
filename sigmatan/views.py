<<<<<<< HEAD
from django.shortcuts import render

def home(request):
    template_name = "list.html"
    context = {
        'title':'welcome',
    }
    return render(request, template_name, context)
=======
from django.shortcuts import render

def home(request):
    template_name = "home.html"
    context = {
        'title':'welcome',
    }
    return render(request, template_name, context)
>>>>>>> d8af0e47989b8a6ebd218636cb8e83387191bc18
