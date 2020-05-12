import csv
PremBig6 = ["Manchester United", "Chelsea", "Tottenham Hotspur", "Manchester City", "Arsenal", "Liverpool"]
ChampionsLeagueClub = ["FC Barcelona", "Manchester United", "Chelsea", "Tottenham Hotspur", "Manchester City", "Arsenal", "Liverpool", "Juvents", "Paris Saint-Germain",
"Real Madrid", "Napoli", "Milan", "Lazio", "Inter", "Roma", "FC Porto", "Valencia CF", "FC Bayern München"]
with open('playerdata.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        elif line_count < 50000:
            if (row[9] in ChampionsLeagueClub and int(row[3]) < 25 and int(row[3]) > 20):
                print(f'\t{row[2]} is {row[3]} years old, and plays for {row[9]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')