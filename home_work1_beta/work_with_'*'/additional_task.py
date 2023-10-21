import os

def count_files_and_dirs(path: str, is_walk=False) -> dict:
    if is_walk:
        for root, dir, files in os.walk(path):
            path


