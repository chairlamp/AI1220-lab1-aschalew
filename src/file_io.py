# file_io.py
import os
import base64

def encode_file(path):
    """Read a file from disk and return its base64-encoded contents as text.

    Assumes the provided path points to a readable file.

    Args:
        path (str): Absolute or relative path to the file to encode.

    Returns:
        str: Base64 representation of the file contents.
    """
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def list_files(dirpath):
    """Yield file names and paths for all regular files in a directory.

    Args:
        dirpath (str): Directory to scan for files.

    Yields:
        tuple[str, str]: Filename and absolute or relative path for each file.
    """
    for name in os.listdir(dirpath):
        path = os.path.join(dirpath, name)
        if os.path.isfile(path):
            yield name, path
