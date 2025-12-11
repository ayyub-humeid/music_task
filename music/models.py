from django.db import models

# Create your models here.
# 1. (Artist)
class Artist(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)
    birth_year = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name

# 2.  (Album)
class Album(models.Model):
    title = models.CharField(max_length=250)
    release_date = models.DateField()
    
    #: 3 ForeignKey  Artist => album belongs to Artist 
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    
    def __str__(self):
        return f"{self.title} by {self.artist.name}"

# 3. Model (Song)
class Song(models.Model):
    title = models.CharField(max_length=250)
    duration = models.DurationField(null=True, blank=True)
    track_number = models.IntegerField()
    
    #: ForeignKey =>song belongs to album  Album 
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    
    def __str__(self):
        return f"{self.title} ({self.album.title})"
    
    class Meta:
        ordering = ['track_number']