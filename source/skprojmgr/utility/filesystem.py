import os
import pathlib


def create_dir(path):
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    if os.path.exists(path):
        return "DIR(s) successfully created"
    else:
        return "Some errors expired... dir(s) didn`t create"
