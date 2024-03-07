# NOTES

### Backend architecture

- `smallingo-django` should be an API that handles video upload, data-extraction and data-retrieval. This API is to be consumed from the frontend.
- Ideally, `smallingo-django` should be defined in a docker-compose file along all it's required services
- Data storage will be SQL

### Checkpoints

##### Checkpoint 1 (remember last url)
- python

##### Checkpoint 2 (duration + dimensions)
- [moviepy](https://github.com/Zulko/moviepy)

##### Checkpoint 3 (extract 15 seconds audio fragment from video)
- [moviepy](https://github.com/Zulko/moviepy)

##### Checkpoint 4 (speech to text + text translation)
- https://cloud.google.com/speech-to-text/pricing
- https://cloud.google.com/translate/pricing

##### Checkpoint 5 (spanish translated text to speech)
- https://cloud.google.com/text-to-speech

##### Checkpoint 6 (extract the first frame of the video as image)
- [moviepy](https://github.com/Zulko/moviepy)

##### Checkpoint 7 (OCR from image)
- either [this](https://cloud.google.com/vision/docs/ocr) or [this](https://cloud.google.com/video-intelligence/docs/text-detection#request_text_detection_for_video_from_a_local_file)

### Draft model for videos

```
from django.db import models

class SmallingoVideo(models.Model):
    # checkpoint 1
    url = models.URLField()
    
    # checkpoint 2
    duration = models.DurationField()
    pixels_tall = models.PositiveIntegerField()
    
    # checkpoint 3
    audio_fragment = models.FileField(upload_to='audio/')
    
    # checkpoint 4
    audio_fragment_text = models.TextField()
    
    # checkpoint 5
    audio_fragment_speech = models.FileField(upload_to='translation/')
    
    # checkpoint 6
    video_thumbnail = models.ImageField(upload_to='thumbnails/')
    
    # checkpoint 7
    video_ocr = models.TextField()
```
