import os


def get_latest_file_from_type(path: str, file_type: str) -> str:
    """
    Returns the path of the latest file from the given path with the given file type.
    """
    files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith(file_type)]
    return max(files, key=os.path.getctime)
