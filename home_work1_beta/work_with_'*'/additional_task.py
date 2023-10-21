import os



def count_files_and_dirs(any_path: str, is_walk=False) -> dict:

"""
Функция, которая считает количество файлов и папок с помощью рекурсии и лист компрехеншен
"""
    data_dict = {"files": None, "folders": None}

    if is_walk:
        data_dict["files"] = len([f if os.path.isfile(os.path.join(any_path, f))
                 else count_files_and_dirs(os.path.join(any_path, f))
                 for f in os.listdir(any_path)])
        data_dict["folders"] = len([f for f in os.listdir(any_path)
                if os.path.isdir(os.path.join(any_path, f))])
        return data_dict
    data_dict["files"] = len([f for f in os.listdir(any_path) if os.path.isfile(os.path.join(any_path, f))])
    data_dict["folders"] = len([f for f in os.listdir(any_path)
                                if os.path.isdir(os.path.join(any_path, f))])
    return data_dict

print(count_files_and_dirs('/home/deniskhudyakov/PycharmProjects/SkyPro_homework/home_work1_beta', True))

print(count_files_and_dirs(os.getcwd()))