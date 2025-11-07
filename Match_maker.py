players = ['Charlie', 'Alice', 'Dylan', 'Bob', 'Jansen']
y = 1
for x in players:
    for c in range(y, len(players)):
        print(f'{x} vs {players[c]}')
    y += 1