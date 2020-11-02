import json
import pathlib

INPUT_DATABASE_FOLDER = "../database"


def read_existing_entries():
    db_root = pathlib.Path(INPUT_DATABASE_FOLDER)
    def get_files_from_all_subdirs(directory : pathlib.Path):
        json_files = []
        for target in directory.iterdir():


    files = get_files_from_all_subdirs(db_root)

    print(db_root.exists())

    pass


if __name__ == '__main__':
    print(read_existing_entries())
    pass
