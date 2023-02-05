from django.db import models

# Create your models here.
class Video(models.Model):
    video_id = models.IntegerField(db_index=True, null=False,blank=False)
    title = models.CharField(max_length=300, null=True,blank=True )
    description = models.TextField(max_length=1000, null=True,blank=True)
    published_at = models.DateTimeField()
    channelId = models.CharField(max_length=200, null=False,blank=False)
    channelTitle = models.CharField(max_length=200, null=True, blank=True)
    thumbnailsUrl = models.URLField()
    db_entry_created = models.DateField(auto_now_add=True, null=True, blank=True)
    # number_of_views = models.IntegerField()
    
    class Meta:
        ordering = ['-published_at']
