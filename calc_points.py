from operator import concat


league_table = []
teams = []


def win(winner, looser):
    if not any(winner in sublist for sublist in league_table):
        data = [winner, 3]
        league_table.append(data)
    else:
        for i, x in enumerate(league_table):
            if winner in x:
                pts = league_table[i][1]
                pts += 3
                league_table[i][1] = pts

    if not any(looser in sublist for sublist in league_table):
        data = [looser, 0]
        league_table.append(data)


def draw(first_team, second_team):
    if not any(first_team in sublist for sublist in league_table):
        data = [first_team, 1]
        league_table.append(data)
    else:
        for i, x in enumerate(league_table):
            if first_team in x:
                pts = league_table[i][1]
                pts += 1
                league_table[i][1] = pts

    if not any(second_team in sublist for sublist in league_table):
        data = [second_team, 1]
        league_table.append(data)
    else:
        for i, x in enumerate(league_table):
            if second_team in x:
                pts = league_table[i][1]
                pts += 1
                league_table[i][1] = pts


def sort_table():
    league_table.sort(key=lambda row: (-row[1], row[0]))
    m = 1
    check = 0
    repeat = 0
    for item in league_table:
        if m == 1:
            print(f'{m}. {item[0]}, {item[1]} pts')
            check = item[1]
            m += 1
        elif item[1] == check:
            repeat += 1
            l = m - repeat
            print(f'{l}. {item[0]}, {item[1]} pts')
            check = item[1]
            m += 1
        else:
            print(f'{m}. {item[0]}, {item[1]} pts')
            check = item[1]
            repeat = 0
            m += 1


def clean_data(games_played):
    games = games_played.split(",")
    striped = list(map(str.strip, games))
    first_team_score = striped[0].split(" ")
    second_team_score = striped[1].split(" ")
    first = ""
    second = ""

    for i in range(len(first_team_score) - 1):
        first = first + ' ' + first_team_score[i]

    for i in range(len(second_team_score) - 1):
        second = second + ' ' + second_team_score[i]

    i = int(first_team_score[(len(first_team_score) - 1)].strip())
    j = int(second_team_score[(len(second_team_score) - 1)].strip())
    first = first.strip()
    second = second.strip()
    if i > j:
        win(first, second)
    elif j > i:
        win(second, first)
    else:
        draw(first, second)


def score(games_played):
    if len(games_played) < 1:
        clean_data(games_played)
    else:
        for match in games_played:
            clean_data(match)
    sort_table()
