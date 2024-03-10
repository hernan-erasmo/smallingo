from celery.result import AsyncResult
from pprint import pprint
from core import app as celery_app
from core.models import SmallingoVideo
from typing import Dict

def get_task_progress(task_id: str) -> int:
    """
    Return between 0 and 100
    """
    result = AsyncResult(task_id)
    if result.ready():
        return 100
    else:
        task_metadata = celery_app.backend.get_task_meta(result.id)
        return task_metadata.get('result', {}).get('progress', 1)


def sanitize_filename(filename: str) -> str:
    # remove query parameters
    filename = filename.split('?')[0]
    return filename


def format_video_info(sv: SmallingoVideo) -> Dict:
    return {
        "checkpoint_2": {
            "duration": sv.duration,
            "pixels_tall": sv.pixels_tall
        },
        "checkpoint_3": {
            "audio_fragment": sv.audio_fragment.path if sv.audio_fragment else None
        },
        "checkpoint_4": {
            "audio_fragment_text": sv.audio_fragment_text
        },
        "checkpoint_5": {
            "audio_fragment_speech": sv.audio_fragment_speech.path if sv.audio_fragment_speech else None
        },
        "checkpoint_6": {
            "video_thumbnail": sv.video_thumbnail.path if sv.video_thumbnail else None
        },
        "checkpoint_7": {
            "video_ocr": sv.video_ocr
        }
    }
