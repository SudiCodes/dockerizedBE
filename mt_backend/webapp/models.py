from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=100)
    is_adult = models.BooleanField()

    def __str__(self):
        return self.name


class CastMember(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateTimeField()
    added_on = models.DateTimeField(auto_now=True)
    genre = models.ManyToManyField(Genre, related_name='titles')
    casts = models.ManyToManyField(CastMember, related_name='titles')
    rating = models.FloatField()
    poster = models.ImageField()
