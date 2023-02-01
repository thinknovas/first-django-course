from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies': [
        {
          'id': 5,
          'title': 'Jaws',
          'year': 1969,
            
        },
        {
          'id': 6,
          'title': 'Sharknado',
          'year': 1600,  
        },
        {
          'id': 7,
          'title': 'Meg',
          'year': 2000
        }
        ]
}

def movies(request):
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse('Home page')