from celery.result import AsyncResult
from pprint import pprint
from core import app as celery_app


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
