import os

def get_subfolder(any_path: str) -> list:
    folder_list = []
    for folder in os.listdir(any_path):
        full_path = os.path.join(any_path, folder)
        if os.path.isdir(full_path):
            folder_list.append(folder)
            cash = get_subfolder(full_path)
            folder_list.extend(cash)
    return folder_list

def count_files_and_dirs(any_path: str, is_walk=False) -> dict:

    """
    Функция, которая считает количество файлов и папок с помощью рекурсии и лист компрехеншен
    """
    data_dict = {"files": None, "folders": None}

    if is_walk:
        data_dict["files"] = len([f if os.path.isfile(os.path.join(any_path, f))
                 else count_files_and_dirs(os.path.join(any_path, f))
                 for f in os.listdir(any_path)])
        data_dict["folders"] = len(get_subfolder(any_path=any_path))
        return data_dict
    data_dict["files"] = len([f for f in os.listdir(any_path) if os.path.isfile(os.path.join(any_path, f))])
    data_dict["folders"] = len([f for f in os.listdir(any_path)
                                if os.path.isdir(os.path.join(any_path, f))])
    return data_dict

print(count_files_and_dirs('/home/deniskhudyakov/PycharmProjects/SkyPro_homework/home_work1_beta', True))

print(count_files_and_dirs(os.getcwd()))