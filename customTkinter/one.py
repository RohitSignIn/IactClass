a = [[0,1,2],[3,4,5],[6,7,8]]

winner
for i in a:
    winner = True
    for j in i:
        if(game[i] != playerTurn):
            winner = False