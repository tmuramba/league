import get_data
import calc_points

method_of_input = input("""
Hello
Would you like to use stdin(S) or files(F)?
""").lower()

def run(method_of_input):
    if method_of_input == "s":
        print('Please enter data, enter (DONE) when finished')
        games = get_data.typed_data()
        calc_points.score(games)
    elif method_of_input == "f":
        games = get_data.file_data()
        calc_points.score(games)
    else:
        print('Please enter (S) for stdin or (F) for files')
        method_of_input = input('>')

while True:
    run(method_of_input)
    again = input('Would you like to run again? (Y/N)')
    if again.lower() == 'y':
        continue
    else:
        print('Goodbye')
        break

