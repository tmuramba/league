import get_data
import calc_points

games = []
method_of_input = input("""
Hello
Would you like to use stdin(S) or files(F)
""").lower()
while True:
    if method_of_input == "s":
        print('Please enter data, enter Done when finished')
        games = get_data.typed_data()
        calc_points.scorr(games)
        break
    elif method_of_input == "f":
        games = get_data.file_data()
        calc_points.scorr(games)
        break
    else:
        print('Please enter (S) for stdin or (F) for files')
        method_of_input = input('>')