from django.db import models

# Create your models here.
class Projec(models.Model):

    title = models.CharField(max_length= 100)
    description = models.TextField(max_length= 250)
    image = models.ImageField(upload_to='blog/images/',blank=True)
    date = models.DateField(auto_now = True)
    url = models.URLField(blank=True)