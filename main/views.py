from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Movie, Series, People, Cinema, Role
# Create your views here.

def index(request):
    return render(request, 'index.html')

def movies(request):
    movies_list = Movie.objects.order_by('point')
    context = {
        'list': movies_list,
    }
    return render(request, 'movies/list.html', context)

def movie_info(request, movie_id):
    try:    
        movie_info = Movie.objects.filter(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(request, 'movies/info.html', { 'info' : movie_info })

def movie_rate(request, movie_id):
    if request.method == "GET":
        vote = int(request.GET.get('point'))
        if(1<=vote<=10):
            movie_info = Movie.objects.get(pk=movie_id)
            rate = movie_info.point
            rate = ((rate * movie_info.count) + int(vote)) / (movie_info.count + 1)
            return HttpResponse(Movie.objects.filter(id=movie_id).update(point=rate, count=movie_info.count + 1))
        else:
            return HttpResponse('Your vote is out of range')
    else: 
        return HttpResponse('Invalid request')


def series(request):
    series_list = Series.objects.order_by('point')
    context = {
        'list': series_list,
    }
    return render(request, 'series/list.html', context)

def seri_info(request, seri_id):
    try:    
        seri_info = Series.objects.filter(pk=seri_id)
    except Series.DoesNotExist:
        raise Http404("TV Show does not exist")
    return render(request, 'series/info.html', { 'info' : seri_info})

def seri_rate(request, seri_id):
    if request.method == "GET":
        vote = int(request.GET.get('point'))
        if(1<=vote<=10):
            seri_info = Series.objects.get(pk=seri_id)
            rate = seri_info.point
            rate = ((rate * seri_info.count) + int(vote)) / (seri_info.count + 1)
            return HttpResponse(Series.objects.filter(id=seri_id).update(point=rate, count=seri_info.count + 1))
        else:
            return HttpResponse('Your vote is out of range')
    else: 
        return HttpResponse('Invalid request')

def peoples(request):
    people_list = People.objects.order_by('point')
    role_list = Role.objects.order_by('person')
    context = {
        'list': people_list,
        'role': role_list,
    }
    return render(request, 'peoples/list.html', context)

def people_info(request, people_id):
    try:    
        people_info = People.objects.filter(pk=people_id)
        role_list = Role.objects.order_by('person')
        context = {
            'info': people_info,
            'role': role_list,
        }
    except People.DoesNotExist:
        raise Http404("People does not exist")
    return render(request, 'peoples/info.html', context)

def people_rate(request, people_id):
    if request.method == "GET":
        vote = int(request.GET.get('point'))
        if(1<=vote<=10):
            people_info = People.objects.get(pk=people_id)
            rate = people_info.point
            rate = ((rate * people_info.count) + int(vote)) / (people_info.count + 1)
            return HttpResponse(People.objects.filter(id=people_id).update(point=rate, count=people_info.count + 1))
        else:
            return HttpResponse('Your vote is out of range')
    else: 
        return HttpResponse('Invalid request')

def cinemas(request):
    cinema_list = Cinema.objects.order_by('point')
    context = {
        'list': cinema_list
    }
    return render(request, 'cinemas/list.html', context)

def cinema_info(request, cinema_id):
    try:    
        cinema_info = Cinema.objects.filter(pk=cinema_id)
    except Cinema.DoesNotExist:
        raise Http404("Movie Theater does not exist")
    return render(request, 'cinemas/info.html', {'info': cinema_info})

def cinema_rate(request, cinema_id):
    if request.method == "GET":
        vote = int(request.GET.get('point'))
        if(1<=vote<=10):
            cinema_info = Cinema.objects.get(pk=cinema_id)
            rate = cinema_info.point
            rate = ((rate * cinema_info.count) + int(vote)) / (cinema_info.count + 1)
            return HttpResponse(Cinema.objects.filter(id=cinema_id).update(point=rate, count=cinema_info.count + 1))
        else:
            return HttpResponse('Your vote is out of range')
    else: 
        return HttpResponse('Invalid request')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')