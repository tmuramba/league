from pathlib import Path


def typed_data():
    games = []
    while True:
        stdin_data = input('>')
        if stdin_data == "done":
            break
        games.append(stdin_data)
    return games


def file_data():
    position = input('Is file in current directory: Y/N ').lower()
    if position == 'y':
        name = input('Please enter file name ')
        if Path(name).exists():
            return Path(name).read_text().split('\n')
        else:
            print('Please enter full or correct file name')
            return file_data()
    elif position == "n":
        path_name = input('Please enter file path  ')
        if Path(path_name).exists():
            return Path(path_name).resolve().read_text().split('\n')
        else:
            print('Please enter correct file path')
            return file_data()
    else:
        print('Please enter Y/N')
        return file_data()
