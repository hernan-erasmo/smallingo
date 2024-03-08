
def sanitize_filename(filename: str) -> str:
    # remove query parameters
    filename = filename.split('?')[0]
    return filename
