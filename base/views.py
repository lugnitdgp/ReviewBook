from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from movies.models import MovieReview, Movie
from games.models import GameReview, Game
from series.models import EpisodeReview, Series, Episode
from accounts.models import Account

def base(request):
    return render(request, 'base.html')


def search(request):
    context = {}

    
    query = ""

    if request.GET:
        query = request.GET['q']

    context = get_queryset(str(query))
    context['query'] = str(query)
    
    return render(request, 'search_list.html', context)

def home(request):

    context = {}
    moviereview=[]
    gamereview=[]
    episodereview=[]
    movieitems=MovieReview.objects.values('movie','id')
    t={item['movie'] for item in movieitems}
    for h in t:
        obbm = MovieReview.objects.filter(movie=h)
        n=len(obbm)
        moviereview.append([obbm,range(1,n)])
    
    gameitems=GameReview.objects.values('game','id')
    t={item['game'] for item in gameitems}
    for h in t:
        obbg = GameReview.objects.filter(game=h)
        n=len(obbg)
        gamereview.append([obbg, range(1,n)])
    
    episodes=EpisodeReview.objects.values('episode','id')
    t={item['episode'] for item in episodes}
    for h in t:
        obbe = EpisodeReview.objects.filter(game=h)
        n=len(obbe)
        gamereview.append([obbe, range(1,n)])
    

    context={'gamereview':gamereview,'moviereview':moviereview,'episodereview':episodereview}

    return render(request, 'home.html', context)

def select_category(request):
    return render(request, 'select_category.html')

def get_queryset(query):
    queryset = {}
    queries = query.split(" ")
    if query:
        for q in queries:
            movies = Movie.objects.filter(
                    Q(name__icontains=q),
            ).distinct()
            games = Game.objects.filter(
                    Q(name__icontains=q),
            ).distinct()
            series = Series.objects.filter(
                    Q(name__icontains=q),
            ).distinct()
            episodes = Episode.objects.filter(
                    Q(episode_name__icontains=q),
            ).distinct()
            users = Account.objects.filter(
                    Q(first_name__icontains=q),
            ).distinct()

            queryset['movies'] = movies
            queryset['games'] = games
            queryset['series'] = series
            queryset['episodes'] = episodes
            queryset['users'] = users

       

    return queryset
