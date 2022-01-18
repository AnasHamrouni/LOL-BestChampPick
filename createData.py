import sys
import json
import numpy as np

def get_champs():
    with open('Game_Stats_euw1.json', "r") as f_name:
        lol_matchs_data = json.load(f_name)
    currentGameID = "EUW1_5667729846"
    games_champ = []
    currentGame_champ= []
    for v in lol_matchs_data:
        if (currentGameID != v[7]):
            currentGameID = v[7]
            games_champ.append([currentGame_champ[0:5],currentGame_champ[5:10],v[8]])
            currentGame_champ= []
        currentGame_champ.append(v[0])
    return games_champ

def best_pick(myTeam = [62],enemyTeam = []):
    games_champ = get_champs()
    iteration = 0
    min4 = []
    min3 = []
    min2 = []
    min1 = []
    for v in games_champ:
        m = set.intersection(set(myTeam), set(v[0]))
        e = set.intersection(set(myTeam), set(v[1]))
        lenm=len(m)
        lene=len(e)
        if((lenm==4) or (lene==4)):
            min4.append(games_champ[iteration])
            min3.append(games_champ[iteration])
            min2.append(games_champ[iteration])
            min1.append(games_champ[iteration])
        elif((lenm==3) or (lene==3)):
            min3.append(games_champ[iteration])
            min2.append(games_champ[iteration])
            min1.append(games_champ[iteration])
        elif((lenm==2) or (lene==2)):
            min2.append(games_champ[iteration])
            min1.append(games_champ[iteration])
        elif((lenm==1) or (lene==1)):
            min1.append(games_champ[iteration])
        iteration += 1
    if (len(min4) != 0):
        return min4
    elif (len(min4) != 0):
        return min3
    elif(len(min4) != 0):
        return min2
    elif(len(min4) != 0):
        return min1
