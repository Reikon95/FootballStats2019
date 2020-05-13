import csv
PremBig6 = ["Manchester United", "Chelsea", "Tottenham Hotspur", "Manchester City", "Arsenal", "Liverpool"]
ChampionsLeagueClub = ["FC Barcelona", "Manchester United", "Chelsea", "Tottenham Hotspur", "Manchester City", "Arsenal", "Liverpool", "Juvents", "Paris Saint-Germain",
"Real Madrid", "Napoli", "Milan", "Lazio", "Inter", "Roma", "FC Porto", "Valencia CF", "FC Bayern München"]
GoodValueClubs = ["Ajax", "Stade Rennais FC", "LOSC Lille"]
with open('playerdata.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    potenitals = []
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        elif line_count < 50000:
            if (row[9] in GoodValueClubs and int(row[3]) < 24 and int(row[3]) > 19):
                print(f'\t{row[2]} is {row[3]} years old, and plays for {row[9]}.')
                potenitals.append(row[2])
            line_count += 1
    print(f'Processed {line_count} lines.')
    print(len(potenitals))