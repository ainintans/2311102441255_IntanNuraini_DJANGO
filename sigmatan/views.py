from django.shortcuts import render

def home(request):
    template_name = "list.html"
    context = {
        'title':'welcome',
    }
    return render(request, template_name, context)