league_table = []
teams = []


def win(first_team, second_team):
    if not any(first_team in sublist for sublist in league_table):
        data = []
        data = [first_team, 3]
        league_table.append(data)
    else:
        for i, x in enumerate(league_table):
            if first_team in x:
                position = (i, x.index(first_team))
                pts = league_table[i][1]
                pts += 3
                league_table[i][1] = pts

    if not any(second_team in sublist for sublist in league_table):
        data = []
        data = [second_team, 0]
        league_table.append(data)


def draw(first_team, second_team):
    if not any(first_team in sublist for sublist in league_table):
        data = []
        data = [first_team, 1]
        league_table.append(data)
    else:
        for i, x in enumerate(league_table):
            if first_team in x:
                position = (i, x.index(first_team))
                pts = league_table[i][1]
                pts += 1
                league_table[i][1] = pts

    if not any(second_team in sublist for sublist in league_table):
        data = []
        data = [second_team, 1]
        league_table.append(data)
    else:
        for i, x in enumerate(league_table):
            if second_team in x:
                position = (i, x.index(second_team))
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


def scorr(games_played):
    for match in games_played:
        games = match.split(",")
        striped = list(map(str.strip, games))
        first = striped[0]
        second = striped[1]
        i = int(first[-1])
        j = int(second[-1])
        first = first.rstrip(first[-1])
        second = second.rstrip(second[-1])
        if i > j:
            first = first.strip()
            second = second.strip()
            win(first, second)
        elif j > i:
            first = first.strip()
            second = second.strip()
            win(second, second)
        else:
            first = first.strip()
            second = second.strip()
            draw(first, second)
    sort_table()

