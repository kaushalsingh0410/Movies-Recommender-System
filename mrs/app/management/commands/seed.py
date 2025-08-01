from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.management import call_command
from django.db import connection
from app.models import *
import csv,ast

class Command(BaseCommand):
    help = 'Creating Data ......'
    models = [Genres,Casts,Collections,Countries,Directors,Screenplay,Crew,SpokenLanguages,Video,Backdrop,Poster,ProductionCompanies]
    files = ['genres.csv',"casts.csv","collections.csv","countries.csv","directors.csv","screenplayers.csv","crews.csv","spoken_languages.csv","videos.csv","backdrops.csv","posters.csv","production_companies.csv"]
    
    def load_data_from_csv(self,model,path):
        self.stdout.write(f"Start with {path.split('.')[0].upper()} ......")
        path =  (settings.BASE_DIR / 'assets' / path).resolve()
        with open(path,'r',newline='',encoding = 'utf-8') as fp:
            reader = csv.DictReader(fp)
            bulk = [model(*[y if not y.isdigit() else int(y) for x,y in row.items()]) for row in reader]
            model.objects.bulk_create(bulk)
        self.stdout.write(f"Loaded {len(bulk)} records into {model._meta.db_table}")  
    
          
    def handle(self, *args, **options):
        self.stdout.write('Creating Data ......')
        for i in range(len(self.models)):
            self.load_data_from_csv(self.models[i],self.files[i])
        self.stdout.write(f"Loading movies")
        path = (settings.BASE_DIR / 'assets' / 'row_data.csv').resolve()
        with open(path,'r',newline='',encoding = 'utf-8') as fp:
            reader = csv.DictReader(fp)
            for row in reader:
                self.stdout.write(f"Loading movies")
                movies = Movies(
                    id = row['id'],
                    adult = row['adult'],
                    budget = row['budget'],
                    backdrop_path = row['backdrop_path'],
                    poster_path = row['poster_path'],
                    homepage = row['homepage'],
                    title = row['title'],
                    overview = row['overview'],
                    popularity = row['popularity'],
                    release_date = row['release_date'],
                    runtime = row['runtime'],
                    tageline = row['tagline'],
                    vote_average = row['vote_average'],
                    vote_count = row['vote_count'],
                    revenue = row['revenue'],
                    keyword = ast.literal_eval(row['keywords']),
                    belongsToCollection = Collections.objects.get(name =  ast.literal_eval(row['belongs_to_collection'])['name']) if row['belongs_to_collection'] != '' else None )
                movies.save()
                
                movies.genres.set(  Genres.objects.filter(name__in =  ast.literal_eval(row['genres'])))
                movies.country.set(  Countries.objects.filter(name__in =  ast.literal_eval(row['origin_country'])))
                movies.languages.set(  SpokenLanguages.objects.filter(name__in = ast.literal_eval(row['spoken_languages'])))

                movies.casts.set(  Casts.objects.filter(name__in =  [name[0] for name in ast.literal_eval(row['cast'])]))
                movies.directors.set(  Directors.objects.filter(name__in =  [name[0] for name in ast.literal_eval(row['director'])]))
                movies.screenplay.set(  Screenplay.objects.filter(name__in = [name[0] for name in ast.literal_eval(row['screenplay'])]))
                movies.company.set(  ProductionCompanies.objects.filter(name__in = [name[0] for name in ast.literal_eval(row['production_companies'])]))
                movies.poster.set(  Poster.objects.filter(file_path__in = [name[2] for name in ast.literal_eval(row['posters'])]))
                movies.backdrop.set(  Backdrop.objects.filter(file_path__in = [name[2] for name in  ast.literal_eval(row['backdrops'])]))
                movies.video.set(  Video.objects.filter(key__in = [name[1] for name in ast.literal_eval(row['videos'])]))
                movies.crew.set(  Crew.objects.filter(name__in = [name[0] for name in ast.literal_eval(row['crew'])]))
                

        
        