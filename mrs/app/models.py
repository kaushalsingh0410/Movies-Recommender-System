from django.db import models

class Genres(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,verbose_name = 'Genre Name')
    
    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        db_table = 'Genres'
        
    def __str__(self):
        return self.name

class Casts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,verbose_name = 'Actor Name')
    profile_photo = models.CharField(max_length=100,verbose_name = 'Photo Path')
    cast_id = models.CharField(verbose_name = 'Cast Id')
    character = models.CharField(max_length=100,verbose_name = 'Character Name')
    credit_id = models.CharField(max_length=100,verbose_name = 'Credit Id')
    
    class Meta:
        verbose_name = 'Cast'
        verbose_name_plural = 'Casts'
        db_table = 'Casts'
    
    
    def __str__(self):
        return self.name

class Collections(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,verbose_name='Collection Name')
    collection_id = models.PositiveBigIntegerField(verbose_name='Collection Id')
    poster = models.CharField(max_length=100,verbose_name='Collection poster')
    backdrop = models.CharField(max_length=100,verbose_name='Collection Backdrop')
    
    class Meta:
        verbose_name = 'Collection'
        verbose_name_plural = 'Collections'
        db_table = 'Collections'
    
    def __str__(self):
        return self.name
    
class Countries(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,verbose_name = 'Country Name')
    
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        db_table = 'Countries'   
    
    def __str__(self):
        return self.name

class Directors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,verbose_name = 'Directors Name')
    profile_path = models.CharField(max_length=100,verbose_name = 'Photo Path')
    director_id = models.PositiveBigIntegerField(verbose_name = 'Directors Id')
    department = models.CharField(max_length=100,verbose_name = 'Department')
    job = models.CharField(max_length=100,verbose_name = 'Job')
    credit_id = models.CharField(max_length=100,verbose_name = 'Credit Id')
    
    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directors'
        db_table = 'Directors'
    
    def __str__(self):
        return self.name

class Screenplay(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,verbose_name = 'Screenplay Name')
    profile_path = models.CharField(max_length=100,verbose_name = 'Photo Path')
    screenplay_id = models.PositiveBigIntegerField(verbose_name = 'Screenplay Id')
    department = models.CharField(max_length=100,verbose_name = 'Department')
    credit_id = models.CharField(max_length=100,verbose_name = 'Credit Id')
    job = models.CharField(max_length=100,verbose_name = 'Job')
    
    class Meta:
        verbose_name = 'Screenplay'
        verbose_name_plural = 'Screenplayers'
        db_table = 'Screenplayers'
    
    def __str__(self):
        return self.name


class Crew(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,verbose_name = 'Crew Name')
    profile_path = models.CharField(max_length=100,verbose_name = 'Photo Path')
    crew_id = models.PositiveBigIntegerField(verbose_name = 'Crew Id')
    department = models.CharField(max_length=100,verbose_name = 'Department')
    credit_id = models.CharField(max_length=100,verbose_name = 'Credit Id')
    job = models.CharField(max_length=100,verbose_name = 'Job')
    
    class Meta:
        verbose_name = 'Crew'
        verbose_name_plural = 'Crews'
        db_table = 'Crews'
    
    def __str__(self):
        return self.name
    
class SpokenLanguages(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,verbose_name='Language')
    
    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'
        db_table = 'Languages'
    
    def __str__(self):
        return self.name

class Video(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,verbose_name='Video Name')
    key = models.CharField(max_length=100,verbose_name='Video key')
    site = models.CharField(max_length=100,verbose_name='Site')
    size = models.CharField(max_length=100,verbose_name='Size')
    video_id = models.CharField(max_length=100,verbose_name='Video Id')
    
    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
        db_table = 'videos'
    
    def __str__(self):
        return self.name

class Backdrop(models.Model):
    id = models.AutoField(primary_key=True)
    file_path = models.CharField(max_length=100,verbose_name='Photo Path')
    height = models.PositiveBigIntegerField(verbose_name='Height')
    width = models.PositiveBigIntegerField(verbose_name='Width')
    
    class Meta:
        verbose_name = 'Backdrop'
        verbose_name_plural = 'Backdrops'
        db_table = 'Backdrops'
    
    def __str__(self):
        return self.file_path


class Poster(models.Model):
    id = models.AutoField(primary_key=True)
    file_path = models.CharField(max_length=100,verbose_name='Photo Path')
    height = models.PositiveBigIntegerField(verbose_name='Height')
    width = models.PositiveBigIntegerField(verbose_name='Width')
    aspect_ratio = models.FloatField(max_length=100,verbose_name='Aspect Ratio')
    
    class Meta:
        verbose_name = 'Poster'
        verbose_name_plural = 'Posters'
        db_table = 'Posters'
    
    def __str__(self):
        return self.file_path
    
class ProductionCompanies(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,verbose_name='Production Company Name')
    poster = models.CharField(max_length=100,verbose_name='Photo Path')
    country = models.CharField(max_length=100,null = True,blank = True,verbose_name='country Name')
    
    class Meta:
        verbose_name = 'Production Company'
        verbose_name_plural = 'Production Companies'
        db_table = 'Production Companies'
    
    def __str__(self):
        return self.name
    
class Movies(models.Model):
    id = models.BigAutoField(primary_key=True,verbose_name='Id')
    adult = models.BooleanField(verbose_name='Adult')
    budget = models.BigIntegerField(verbose_name='Budget')
    backdrop_path = models.CharField(verbose_name='backdrop_path')
    poster_path = models.CharField(verbose_name='poster_path')
    homepage = models.URLField(blank = True,null = True,verbose_name='Homepage')
    title = models.CharField(max_length = 255,verbose_name='Title')
    keyword = models.TextField(verbose_name='Keyword')
    overview = models.TextField(verbose_name='Overview')
    popularity = models.FloatField(verbose_name='Popularity')
    release_date = models.DateField(verbose_name='Release Date')
    runtime = models.PositiveIntegerField(verbose_name='Run Time')
    tageline = models.TextField(verbose_name='Tage Line')
    vote_average = models.FloatField(verbose_name='Vote Average')
    vote_count = models.IntegerField(verbose_name='Vote Count')
    revenue = models.BigIntegerField(verbose_name='Revenue')
    belongsToCollection = models.ForeignKey(Collections,
                                            on_delete = models.SET_NULL,blank = True, null= True,
                                            related_name = 'collection',
                                            verbose_name='Collection')
    genres = models.ManyToManyField(
        Genres,
        related_name='genre',
        verbose_name='Genres'
        )
    casts = models.ManyToManyField(
        Casts,
        related_name='cast',
        verbose_name='Casts'
        )
    country = models.ManyToManyField(
        Countries,
        related_name='country',
        verbose_name='Countries'
        )
    directors = models.ManyToManyField(
        Directors,
        related_name='director',
        verbose_name='Directors')
    screenplay = models.ManyToManyField(
        Screenplay,
        related_name='screenplay',
        verbose_name='Screenplay'
        )
    languages = models.ManyToManyField(
        SpokenLanguages,
        related_name='languages',
        verbose_name='Languages'
        )
    company = models.ManyToManyField(
        ProductionCompanies,
        related_name='company',
        verbose_name='ProductionCompanies'
        )
    poster = models.ManyToManyField(
        Poster,
        related_name='poster',
        verbose_name='Poster'
        )
    backdrop = models.ManyToManyField(
        Backdrop,
        related_name='backdrop',
        verbose_name='Backdrop'
        )
    video = models.ManyToManyField(
        Video,
        related_name='video',
        verbose_name='Video'
        )

    
    crew = models.ManyToManyField(
        Crew,
        related_name='crew',
        verbose_name='Crew'
        )
    
    
    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        db_table = 'Movies'
    def __str__(self):
        return self.title
    
