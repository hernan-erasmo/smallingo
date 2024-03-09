from django.db import models
from django.conf import settings


class SmallingoVideo(models.Model):
    # checkpoint 1
    url = models.URLField(max_length=65535)
    
    # required for extracting info
    uploaded_file = models.FileField(blank=True, null=True, upload_to=settings.VIDEO_DIR)

    # checkpoint 2
    duration = models.DurationField(blank=True, null=True)
    pixels_tall = models.PositiveIntegerField(blank=True, null=True)
    
    # checkpoint 3
    audio_fragment = models.FileField(blank=True, null=True, upload_to=settings.AUDIO_DIR)
    
    # checkpoint 4
    audio_fragment_text = models.TextField(blank=True, null=True)
    
    # checkpoint 5
    audio_fragment_speech = models.FileField(blank=True, null=True, upload_to=settings.AUDIO_TRANSLATION_DIR)
    
    # checkpoint 6
    video_thumbnail = models.ImageField(blank=True, null=True, upload_to=settings.THUMBNAIL_DIR)
    
    # checkpoint 7
    video_ocr = models.TextField(blank=True, null=True)
