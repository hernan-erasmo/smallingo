import os
import traceback
from datetime import datetime, timedelta
from typing import Optional

import requests
from celery import chain
from moviepy.editor import VideoFileClip

from django.core.files.base import ContentFile
from core import app as celery_app
from core.models import SmallingoVideo
from core.utils import sanitize_filename


# TODO(Hernan) need to find a way to normalize original video names to be consistent
# with their parsed content, and also to avoid having duplicate videos.
@celery_app.task(bind=True)
def download_original_video(self, video_id: int) -> None:
    def on_download_success():
        chain(
            populate_duration_and_height.s(kwargs={"video_id": video_id}),
            populate_audio_fragment.s(kwargs={"video_id": video_id}),
            populate_video_thumbnail.s(kwargs={"video_id": video_id})
        ).apply_async()

    try:
        smallingo_video = SmallingoVideo.objects.get(id=video_id)
        file_url = smallingo_video.url

        print(f"GETting file at {file_url}")
        with requests.get(file_url, stream=True) as response:
            if response.status_code == 200:
                print(f"Successfully got {file_url}")
                file_content = response.content
                file_name = f"{sanitize_filename(os.path.basename(file_url))}_{datetime.now().strftime('%y%m%d%H%M%S%f')}"
                smallingo_video.uploaded_file.save(file_name, ContentFile(file_content), save=True)
                smallingo_video.save()
            else:
                print(f"Failed to download file from {file_url}: HTTP status code {response.status_code}")
    except SmallingoVideo.DoesNotExist:
        print(f"SmallingoVideo with id={video_id} does not exist.")
    except Exception:
        print(traceback.format_exc())
    else:
        on_download_success()


@celery_app.task(bind=True)
def populate_duration_and_height(self, *args, **kwargs) -> None:
    video_id = kwargs.get('kwargs', {}).get('video_id')
    try:
        smallingo_video = SmallingoVideo.objects.get(id=video_id)
        print("Instantiating video object")
        video = VideoFileClip(smallingo_video.uploaded_file.path)
        smallingo_video.duration = timedelta(seconds=video.duration)
        smallingo_video.pixels_tall = video.size[1]
        print(f"Saving video object with duration = {smallingo_video.duration} and height = {smallingo_video.pixels_tall}")
        smallingo_video.save()
        video.close()
    except SmallingoVideo.DoesNotExist:
        print(f"SmallingoVideo with id={video_id} does not exist.")
    except Exception as ex:
        traceback.print_exception(ex)


@celery_app.task(bind=True)
def populate_audio_fragment(self, *args, **kwargs) -> None:
    video_id = kwargs.get('kwargs', {}).get('video_id')
    try:
        smallingo_video = SmallingoVideo.objects.get(id=video_id)
        duration = smallingo_video.duration

        print("Calculating audio_start and audio_end")
        if duration > timedelta(seconds=45):
            audio_start = 30
            audio_end = 45
        elif timedelta(seconds=15) < duration <= timedelta(seconds=45):
            audio_start = max(duration - 15, 0)
            audio_end = duration
        else:
            audio_start = 0
            audio_end = duration
        print(f"audio_start = {audio_start}, audio_end = {audio_end}")

        print("Creating audio clip")
        video = VideoFileClip(smallingo_video.uploaded_file.path)
        audio_fragment = video.subclip(audio_start, audio_end).audio

        video_name = smallingo_video.uploaded_file.name.split('/')[-1]
        audio_filename = smallingo_video.audio_fragment.field.upload_to + '/' + video_name + '.mp3'

        print("Writing audio file at {audio_filename}")
        audio_fragment.write_audiofile(audio_filename)
        smallingo_video.audio_fragment.name = audio_filename
        smallingo_video.save()
        video.close()
    except SmallingoVideo.DoesNotExist:
        print(f"SmallingoVideo with id={video_id} does not exist.")
    except Exception as ex:
        traceback.print_exception(ex)


@celery_app.task(bind=True)
def populate_video_thumbnail(self, *args, **kwargs) -> None:
    video_id = kwargs.get('kwargs', {}).get('video_id')
    try:
        smallingo_video = SmallingoVideo.objects.get(pk=video_id)
        print("Instantiating video object")
        video = VideoFileClip(smallingo_video.uploaded_file.path)
        video_name = smallingo_video.uploaded_file.name.split('/')[-1]
        frame_filename = smallingo_video.video_thumbnail.field.upload_to + '/' + video_name + '.png'
        print("Extracting first frame from video")
        video.save_frame(frame_filename, t=0)
        smallingo_video.video_thumbnail.name = frame_filename
        smallingo_video.save()
        video.close()
    except SmallingoVideo.DoesNotExist:
        print(f"SmallingoVideo with id={video_id} does not exist.")
    except Exception as ex:
        traceback.print_exception(ex)
