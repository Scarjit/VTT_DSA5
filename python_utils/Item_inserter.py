import json
import pathlib
import pprint
INPUT_DATABASE_FOLDER = "../database"


def read_existing_entries(input_databse):
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
            with open("/".join(f.parts),encoding="utf-8") as in_file:
                r_dict[f.name] = json.load(in_file)
        except Exception as _e:
            print(f"can not open {f.name}, due to error: {_e}")

    pprint.pprint(r_dict)



    pass


if __name__ == '__main__':
    print(read_existing_entries(INPUT_DATABASE_FOLDER + "/items"))

    pass
