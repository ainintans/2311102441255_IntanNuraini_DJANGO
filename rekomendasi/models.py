from django.db import models

class Drakor(models.Model):
    judul = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    tahun = models.IntegerField()
    sinopsis = models.TextField()
    rating = models.FloatField()
    gambar = models.ImageField(upload_to='poster_drakor/', blank=True, null=True)

    def __str__(self):
        return self.judul
