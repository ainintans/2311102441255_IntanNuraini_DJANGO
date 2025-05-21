from django.db import models

class Drama(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField()
    
    def __str__(self):
        return self.title
