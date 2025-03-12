from django.shortcuts import render

def home(request):
    template_name = "home.html"
    context = {
        'title':'welcome',
    }
    return render(request, template_name, context)
