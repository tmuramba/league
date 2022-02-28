from pathlib import Path
games = []


def typed_data():
    while True:
        stdin_data = input('>').lower()
        if stdin_data == "done":
            break
        games.append(stdin_data)
    return games


def file_data():
    position = input('Is file in current directory: Y/n ').lower()
    if position == 'y':
        name = input('Please enter file name ')
        if Path(name).exists():
            games = Path(name).read_text()
            games = games.split('\n')
            return games
        else:
            print('Please enter full or correct file name')
            file_data()
    elif position == "n":
        path_name = input('Please enter file path  ')
        if Path(path_name).exists():
            games = Path(path_name).resolve().read_text()
            games = games.split('\n')
            return games
        else:
            print('Please enter correct file path')
            file_data()
    else:
        print('Please enter yes or no')
        file_data()
