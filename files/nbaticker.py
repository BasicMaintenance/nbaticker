#ASYNC VARIATION

import copy
import asyncio
from nba_api.live.nba.endpoints import scoreboard

board = scoreboard.ScoreBoard()
games = board.games.get_dict()
scoreSheet = [[1,2,3,4] for i in range(len(games))] # 2-Dimensional array; 4 column, rows dependent on number of games being played.

lastScoreSheet = []

# Function to fill [x][4] score sheet array

def fillScoreSheet(a, games):

    x = 0

    while x<len(games):
        a[x][0]=games[x]['homeTeam']['teamTricode']
        a[x][1]=games[x]['homeTeam']['score']
        a[x][2]=games[x]['awayTeam']['teamTricode']
        a[x][3]=games[x]['awayTeam']['score']
        x += 1

# Prints scoresheet

def printing(sc):
    with open("scoreboard.txt", "w") as file:
        file.write("\n".join(str(value) for row in sc for value in row))
        file.write("\n")

# Fills a new scoresheet, compares to last, prints if scores have updated and moves current values to last sheet.

async def scoreBoardUpdate():
    global lastScoreSheet

    while True:
        board = scoreboard.ScoreBoard()
        games = board.games.get_dict()

        fillScoreSheet(scoreSheet, games)
        newScoreSheet = copy.deepcopy(scoreSheet)

        if newScoreSheet != lastScoreSheet:
            printing(newScoreSheet)
            lastScoreSheet = copy.deepcopy(newScoreSheet)

        await asyncio.sleep(1) 

asyncio.run(scoreBoardUpdate())










