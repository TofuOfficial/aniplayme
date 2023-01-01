from django.db import models

# Create your models here.
class Episode(models.Model):
    video_title = models.CharField(max_length=30)