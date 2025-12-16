import os
import shutil
from pathlib import Path
from random import randint, choice
from string import ascii_letters

DESKTOP = Path.home() / "Desktop"
MAIN_FOLDER_PATH = DESKTOP / "Organized"

RANDOM_FILES = False

EXTENSION_MAP = {
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".gif": "Images",
    ".svg": "Images",
    ".heic": "Images",

    ".mp4": "Videos",
    ".wav": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",

    ".mp3": "Music",
    ".wav": "Music",
    ".aac": "Music",
    ".flac": "Music",

    ".pdf": "PDF",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".pptx": "Documents",
    ".xls": "Documents",
    ".xlsx": "Documents",

    ".zip": "Archives",
    ".rar": "Archives",
}

def createFolder(path: Path, name: str):
    createdFolder = path / name
    createdFolder.mkdir(exist_ok=True, parents=True)

    return createdFolder

def createTestFiles():
    for i in range(randint(5, 10)):
        name = "".join(choice(ascii_letters) for _ in range(5))

        path = DESKTOP / (name + choice(list(EXTENSION_MAP.keys())))
        path.touch()

def main():
    if RANDOM_FILES: createTestFiles()
    folders = {} # {Videos: [...], Documents: [...]}
    filelist = os.listdir(DESKTOP)

    for i in filelist:
        for j in EXTENSION_MAP:

            if not i.lower().endswith(j):
                continue

            if EXTENSION_MAP[j] not in folders:
                folders[EXTENSION_MAP[j]] = [i]
                continue

            folders[EXTENSION_MAP[j]].append(i)

    for i in folders:
        folder = createFolder(MAIN_FOLDER_PATH, i)

        for j in folders[i]:
            shutil.move(DESKTOP / j, folder)

if __name__ == "__main__":
    main()
