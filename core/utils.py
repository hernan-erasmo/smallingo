import os
from datetime import datetime
from typing import Optional

from django.core.files.base import ContentFile
from core.models import SmallingoVideo

import requests


def sanitize_filename(filename: str) -> str:
    # remove query parameters
    filename = filename.split('?')[0]
    return filename

# TODO(Hernan) need to find a way to normalize original video names to be consistent
# with their parsed content, and also to avoid having duplicate videos.
def download_original_video(model_id: int) -> Optional[str]:
    try:
        model_instance = SmallingoVideo.objects.get(id=model_id)
        file_url = model_instance.url

        print(f"GETting file at {file_url}")
        response = requests.get(file_url)
        if response.status_code == 200:
            print(f"Successfully got {file_url}")
            file_content = response.content
            file_name = f"{sanitize_filename(os.path.basename(file_url))}_{datetime.now().strftime('%y%m%d%H%M%S%f')}"
            model_instance.uploaded_file.save(file_name, ContentFile(file_content), save=True)
            model_instance.save()
            return file_name
        else:
            print(f"Failed to download file from {file_url}: HTTP status code {response.status_code}")
    except SmallingoVideo.DoesNotExist:
        print(f"Model with id={model_id} does not exist.")
