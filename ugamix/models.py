from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=250)

    def __str__(self):
        return self.category_name

class Movie(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    movie_name = models.CharField(max_length=250)
    movie_file = models.FileField()
    movie_photo = models.FileField()
    movie_description = models.TextField(max_length=10000)
    movie_rate = models.IntegerField(default=0)
    movie_year = models.IntegerField(default=0)
    date_uploaded = models.DateField()

    def __str__(self):
        return self.movie_name