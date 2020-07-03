from django.db import models

# Create your models here.
class Songs(models.Model):
    # song title
    title = models.CharField(max_length=255, null=False)
    # name of artist or group/band
    artist = models.CharField(max_length=255, null=False)
    song = models.FileField(upload_to='' , null=True)

    def __str__(self):
        return "{} - {} - {}".format(self.title, self.artist, self.song)