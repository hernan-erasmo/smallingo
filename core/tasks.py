import os
import traceback
from datetime import datetime, timedelta
from typing import Optional

import requests
from moviepy.editor import VideoFileClip

from django.core.files.base import ContentFile
from core.models import SmallingoVideo
from core.utils import sanitize_filename

# TODO(Hernan) need to find a way to normalize original video names to be consistent
# with their parsed content, and also to avoid having duplicate videos.
def download_original_video(video_id: int) -> Optional[str]:
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
                return file_name
            else:
                print(f"Failed to download file from {file_url}: HTTP status code {response.status_code}")
    except SmallingoVideo.DoesNotExist:
        print(f"SmallingoVideo with id={video_id} does not exist.")


def populate_duration_and_height(video_id: int) -> None:
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
