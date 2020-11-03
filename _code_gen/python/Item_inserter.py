# coding: utf-8
import json
import pathlib
import pprint
from pprint import pprint as ppprint

INPUT_DATABASE_FOLDER = "../database"


def read_existing_entries(input_databse):
    """
    reads all subdirs from dir and returns the continjing json files and returns them as dictionary, with the key being
    the file path
    :param input_databse:
    :return: dict
    """
    db_root = pathlib.Path(input_databse)

    def get_files_from_all_subdirs(directory: pathlib.Path):
        json_files = []
        for target in directory.iterdir():
            if target.is_dir():
                json_files.extend(get_files_from_all_subdirs(target))
            else:
                json_files.append(target)
        return json_files

    files = get_files_from_all_subdirs(db_root)
    r_dict = {}
    print(files)
    for f in files:
        try:
            with open("/".join(f.parts), encoding="utf-8") as in_file:
                r_dict[f.parts] = json.load(in_file)
        except Exception as _e:
            print(f"can not open {f.name}, due to error: {_e}")
    return r_dict


if __name__ == '__main__':
    existing_values = read_existing_entries(INPUT_DATABASE_FOLDER + "/items")
    templates = {}
    entries = {}

    for key in existing_values.keys():
        if "_template" in key[-1]:
            templates[key[:-1]] = existing_values[key][0]
        else:
            entries[key] = existing_values[key]
    ppprint(entries.keys())

