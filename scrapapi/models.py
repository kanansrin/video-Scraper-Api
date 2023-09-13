from django.db import models

# Create your models here.

class Scrapa(models.Model):
    id = models.AutoField(primary_key=True)
    channel_id = models.CharField(max_length=100, null=True)
    channel_title = models.CharField(max_length=100, null=True)
    title= models.CharField(max_length=500, null=True)
    video_id = models.CharField(max_length=100, null=True)
    published_at = models.DateTimeField(auto_now_add=True)
    transcript = models.TextField(null=True)
    sentiment = models.CharField(max_length=100, null=True)

    
    def __str__(self):
        return self.title
    