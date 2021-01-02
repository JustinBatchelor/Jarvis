import os


def prepareName(start_index, command_list):
    search_file = ""
    for index in range(start_index, len(command_list)):
        search_file += command_list[index]
        search_file += " "
    return search_file[:-1]


def findFile(path, file):
    results = []
    for root, dirs, files in os.walk(str(path)):
        for name in files:
            compare_name = name.split(".")
            if compare_name[0].lower() == str(file).lower():
                results.append(os.path.join(root, name))
    return results


def findDirectory(path, file):
    results = []
    for root, dirs, files in os.walk(str(path)):
        for name in dirs:
            compare_name = name.split(".")
            if compare_name[0].lower() == str(dirs).lower():
                results.append(os.path.join(root, name))
    return results
