from django.shortcuts import render,redirect
from django.http import HttpResponse
import joblib
import os 
import json
import ast
from django.conf import settings
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Genres,Movies
from random import sample
from django.db.models import Q
from django.contrib import messages
from rapidfuzz.fuzz import ratio    

ids = os.path.join(settings.BASE_DIR,'app','ml_models','ids.joblib') 
indices = os.path.join(settings.BASE_DIR,'app','ml_models','indices.joblib') 
similarity = os.path.join(settings.BASE_DIR,'app','ml_models','similarity.joblib') 

ids = joblib.load(ids) 
indices = joblib.load(indices) 
similarity = joblib.load(similarity) 
genresDictHeader = Genres.objects.all()



def index(request):
    genres = Genres.objects.all()
    genresDict = {}
    for genre in genres:
        movies = sample(list(Movies.objects.filter(genres = genre)),10)
        genresDict[genre] = movies
        
    data = {
        'title':'Index',
        'genresDict':genresDict,
        }
    return render(request,'app/index.html',data)

def genre_movies_ajax(request):
    genre = request.GET.get('genre').replace('-',' ').title()
    page = int(request.GET.get('page',1))
    all_movies = Movies.objects.filter(genres = Genres.objects.get(name__icontains = genre)).values('title','release_date','poster_path','id')
    paginator = Paginator(all_movies , 10)
    movies = paginator.get_page(page)
    return JsonResponse({
        'movies':list(movies),
        'has_next':movies.has_next()
    })
    
def movies_details(request,id):
    movie = Movies.objects.get(id = id)
    genres = [genre.name for genre in movie.genres.all() ]
    directors = [{'name':director.name,'role':'Director'} for director in movie.directors.all() ]
    screenplay = [{'name':play.name,'role':'Screenplay'} for play in movie.screenplay.all() ]
    country = [country.name for country in movie.country.all() ]
    languages = [str(languages.name) for languages in movie.languages.all() ]
    companies = [comp for comp in movie.company.all() ]
    videos = [video for video in movie.video.all() ]
    backdrops = [backdrop for backdrop in movie.backdrop.all() ]
    posters = [poster for poster in movie.poster.all() ]
    companies = [comp for comp in movie.company.all() ]
    casts = [cast for cast in movie.casts.all() ]
    h = movie.runtime//60
    m = movie.runtime%60
    
    recommendtion = sample(sorted(list(enumerate(similarity[indices[id]])), key = lambda x:x[1],reverse = True)[1:20],10)
    recommendtion = list(map(lambda x: int(ids[x[0]]),recommendtion))
    recommendtion = Movies.objects.filter(id__in = recommendtion)
    num_dir_scr = (len(directors)+len(screenplay))
    num_dir_scr = num_dir_scr//4 if num_dir_scr % 4 ==0 else num_dir_scr//4 +1

    crew = directors+screenplay
    crew_set = []
    counter = 0
    for i in range(num_dir_scr):
        temp = []
        for j in range(4):
            try:
                temp.append(crew[counter])
                counter+=1
            except:
                break
        crew_set.append(temp)

    data = {
        'title':f'{movie.title} {movie.release_date.year}',
        'genresDict':genresDictHeader,
        'genres':genres,
        'date':movie.release_date,
        'runtime':f'{h}h {m}m',
        'movie':movie,
        'keyword':ast.literal_eval(movie.keyword),
        'country':country,
        'languages':languages,
        'casts':casts,
        'companies':companies,
        'vote_average':round(movie.vote_average*10),
        'backdrops':backdrops,
        'posters':posters,
        'videos':videos,
        'recommendtion':recommendtion,
        'crews':crew_set,
        }
    return render(request,'app/movie.html',data )

def search(request,key = None):
    if isinstance( key,str):
        title = key.replace('-',' ')
    elif request.method == 'POST':
        title = request.POST.get('title')
    else:
        title = request.GET.get('title')
        
    if not title:
        messages.error(request,"Search field cannot be empty.")
        return redirect(request.META.get('HTTP_REFERER', 'index'))
    all_movies = Movies.objects.filter(Q(title__icontains = title)|Q(genres__name__icontains = title)|Q(keyword__icontains = title)).distinct()
    if not all_movies.first():
        title = title.lower()
        result = []
        
        for movie in Movies.objects.all().prefetch_related('genres'):
            max_score = -1
            full_title = movie.title.lower()
            max_score = max(max_score,ratio(title,full_title))
            
            for sub_title in full_title.split():
                max_score = max(max_score,ratio(title,sub_title))
            for key in ast.literal_eval(movie.keyword):
                max_score = max(max_score,ratio(title,key))
            
            for genre in movie.genres.all():
                max_score = max(max_score,ratio(title,genre.name))
            
            result.append((movie,max_score))
        
        all_movies = sorted(result, key = lambda x:x[1],reverse = True)[:10]
        
        all_movies = list(map(lambda x:x[0],all_movies))
        
    page = request.GET.get('page',1)
    paginator = Paginator(all_movies,10)
    movies =  paginator.get_page(page)
    next = movies.has_next
    previous = movies.has_previous
    
    current_page = movies.number
    total_page = paginator.num_pages
    
    if total_page <=7:
        page_range = range(1,total_page+1)
    else:
        if current_page <= 4:
            page_range = list(range(1,6))+['...',total_page]
        elif current_page >= total_page -3:
            page_range = [1,'...']+list(range(total_page-4,total_page+1))
        else:
            page_range = [1,'...',current_page-1,current_page,current_page+1,'...',total_page]

    data = {
        'title':title,
        'genresDict':genresDictHeader,
        'movies':movies,
        'page_range':page_range,
        'next':next,
        'previous':previous,
        'total_page':total_page,
    }
    
    if isinstance(key,str):
        return render(request,'app/search_page.html',data)
        
    elif request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'app/search_table.html', data)
    return render(request,'app/search_page.html',data)

def videos(request,id):
    movie = Movies.objects.get(id = id)
    videos = [video for video in movie.video.all() ]
    
    data = {
        'title':f'{movie.title} {movie.release_date.year}',
        'genresDict':genresDictHeader,
        'videos':videos,
        
    }
    return render(request,'app/videos.html',data )

def backdrops(request,id):
    movie = Movies.objects.get(id = id)
    backdrops = [backdrop for backdrop in movie.backdrop.all() ]
    
    data = {
        'title':f'{movie.title} {movie.release_date.year}',
        'genresDict':genresDictHeader,
        'backdrops':backdrops,
        
    }
    return render(request,'app/backdrops.html',data )

def posters(request,id):
    movie = Movies.objects.get(id = id)
    posters = [poster for poster in movie.poster.all() ]
    
    data = {
        'title':f'{movie.title} {movie.release_date.year}',
        'genresDict':genresDictHeader,
        'posters':posters,
        
    }
    return render(request,'app/posters.html',data )

def credits(request,id):
    
    movie = Movies.objects.get(id = id)
    title  = f'{movie.title} ({movie.release_date.year})'
    casts = [cast for cast in movie.casts.all()]
    crews = [cre for cre in movie.crew.all() ]
    
    
    data = {
        'title':title,
        'genresDict':genresDictHeader,
        'casts':casts,
        'crews':crews,
    }
    return render(request,'app/credits.html',data)    




