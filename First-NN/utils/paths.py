import logging
import os

from pathlib import Path
from utils.configs import INPUT_FILE_TYPES
from utils.logs import log


def get_filetype(path: str) -> str:
    """
    Checks and returns the file extension for correct file type.

    Args:
        path: str, relative or absolute file path.
    Returns:
        str
    """
    if not os.path.exists(path): 
        msg = f"Path {os.path.basename(path)} doesn't exists at {os.path.dirname(path)}."
        log(msg, FileNotFoundError)
    
    filetype = Path(path).suffix.replace(".", '').lower()

    if filetype not in INPUT_FILE_TYPES:
        msg = f"{filetype} file type is not allowed."
        log(msg, TypeError)

    return filetype
