from django.shortcuts import render
from .models import Shows
# Create your views here.


def shows(request):
    shows = Shows.objects.all()

    context = {
        'shows': shows,
    }

    template = 'shows/shows.html'

    return render(request, template, context)
    
