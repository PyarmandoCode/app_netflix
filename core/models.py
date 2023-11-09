from django.db import models
class Genre(models.Model):
    genre = models.CharField(max_length=30, blank=True, null=True)
    state = models.BooleanField(default=True)
    created_at = models.DateTimeField('created_at', auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.genre)

    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'
        ordering = ['genre']

class TypePerson(models.Model):
    type_person = (
        ('Actor_Actress', 'Actor_Actress'),
        ('Director', 'Director'),
        ('Producer', 'Producer')
    )
    type_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=15, choices=type_person)
    state = models.BooleanField(default=True)
    created_at = models.DateTimeField('created_at', auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.type

    class Meta:
        ordering = ['type']
        verbose_name = 'TypePerson'
        verbose_name_plural = 'TypePerson'


class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    lastname = models.CharField(max_length=180)
    firstname = models.CharField(max_length=180)
    aliases = models.CharField(max_length=80, blank=True, null=True)
    typeperson = models.ForeignKey(TypePerson, on_delete=models.CASCADE, related_name='person')
    photo = models.ImageField(upload_to='person', blank=True, null=True)
    state = models.BooleanField(default=True)
    created_at = models.DateTimeField('created_at', auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.lastname, self.firstname)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'
        ordering = ['firstname']


class Movie(models.Model):
  
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=180)
    sipnosis = models.TextField(blank=True, null=True)
    release_year = models.IntegerField()
    lenguage = models.CharField(max_length=20)
  
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)
    top = models.ImageField(upload_to='movies', blank=True, null=True)

    Actor_Actress = models.ManyToManyField(Person, related_name='actor_actress')
    Director = models.ManyToManyField(Person, related_name='director')
    Producer = models.ManyToManyField(Person, related_name='producer')

    state = models.BooleanField(default=True)
    created_at = models.DateTimeField('created_at', auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.title)

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        ordering = ['title']


class Comments(models.Model):
    comments_id = models.AutoField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    commentmovie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='commentmovie')
    state = models.BooleanField(default=True)

    def __str__(self):
        return '%s' % (self.comment)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['comment']