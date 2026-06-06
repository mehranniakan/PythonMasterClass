from os import mkdir
from pathlib import Path
import shutil
from shutil import SameFileError

source_dir = Path(r"C:\Users\Mehran\Downloads\Telegram Desktop")
base_target_dir = Path(r"C:\Users\Mehran\Downloads\Telegram Desktop")

final_target_dir = base_target_dir / 'sorted'

FILE_CATEGORIES = {

    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],

    "documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],

    "videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],

    "audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],

    "archives": [".zip", ".rar", ".tar", ".gz", ".7z"]

}

final_target_dir.mkdir(parents=True, exist_ok=True)

for file in base_target_dir.rglob('*'):

    if file.parents == base_target_dir:
        continue

    if file.is_file():

        for category, extension in FILE_CATEGORIES.items():

            if file.suffix.lower() in extension:

                new_path = final_target_dir / category
                new_path.mkdir(parents=True, exist_ok=True)

                try:
                    shutil.move(file, new_path / file.name)
                    break
                except SameFileError:
                    pass
