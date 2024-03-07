from django.db import models

class SmallingoVideo(models.Model):
    # checkpoint 1
    url = models.URLField(max_length=65535)
    
    # checkpoint 2
    duration = models.DurationField(blank=True, null=True)
    pixels_tall = models.PositiveIntegerField(blank=True, null=True)
    
    # checkpoint 3
    audio_fragment = models.FileField(blank=True, null=True)
    
    # checkpoint 4
    audio_fragment_text = models.TextField(blank=True, null=True)
    
    # checkpoint 5
    audio_fragment_speech = models.FileField(blank=True, null=True)
    
    # checkpoint 6
    video_thumbnail = models.ImageField(blank=True, null=True)
    
    # checkpoint 7
    video_ocr = models.TextField(blank=True, null=True)
