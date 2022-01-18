import json


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
        currentGame_champ.append(v[1])
    return games_champ

def best_pick(myTeam ,enemyTeam,games_data):
    iteration = 0
    min4 = []
    min3 = []
    min2 = []
    min1 = []
    for v in games_data:
        m = set.intersection(set(myTeam), set(v[0]))
        e = set.intersection(set(myTeam), set(v[1]))
        lenm=len(m)
        lene=len(e)
        if((lenm==4) or (lene==4)):
            min4.append(games_data[iteration])
            min3.append(games_data[iteration])
            min2.append(games_data[iteration])
            min1.append(games_data[iteration])
        elif((lenm==3) or (lene==3)):
            min3.append(games_data[iteration])
            min2.append(games_data[iteration])
            min1.append(games_data[iteration])
        elif((lenm==2) or (lene==2)):
            min2.append(games_data[iteration])
            min1.append(games_data[iteration])
        elif((lenm==1) or (lene==1)):
            min1.append(games_data[iteration])
        iteration += 1
    if (len(min4) != 0):
        return min4
    elif (len(min3) != 0):
        return min3
    elif(len(min2) != 0):
        return min2
    elif(len(min1) != 0):
        return min1
    else:
        return "nothing found"

def get_selected_champ(selectionSession):
    myTeam = []
    enemyTeam = []
    #print(selectionSession["actions"])
    for actor in selectionSession["actions"][0]:
        if(actor["isAllyAction"] is  True):
            myTeam.append(get_champ_name(actor["championId"]))
        else:
            enemyTeam.append(get_champ_name(actor["championId"]))
    return myTeam,enemyTeam

def get_champ_name(id):
    if (id == 266): 
        return "Aatrox"
    elif (id == 103):
        return "Ahri"
    elif (id == 84):
        return "Akali"
    elif (id == 166):
        return "Akshan"
    elif (id == 12):
        return "Al==tar"
    elif (id == 32):
        return "Amumu"
    elif (id == 34):
        return "Anivia"
    elif (id == 1):
        return "Annie"
    elif (id == 523):
        return "Aphelios"
    elif (id == 22):
        return "Ashe"
    elif (id == 136):
        return "AurelionSol"
    elif (id == 268):
        return "Azir"
    elif (id == 432):
        return "Bard"
    elif (id == 53):
        return "Blitzcrank"
    elif (id == 63):
        return "Brand"
    elif (id == 201):
        return "Braum"
    elif (id == 51):
        return "Caitlyn"
    elif (id == 164):
        return "Camille"
    elif (id == 69):
        return "Cassiopeia"
    elif (id == 31):
        return "Chogath"
    elif (id == 42):
        return "Corki"
    elif (id == 122):
        return "Darius"
    elif (id == 131):
        return "Diana"
    elif (id == 119):
        return "Draven"
    elif (id == 36):
        return "DrMundo"
    elif (id == 245):
        return "Ekko"
    elif (id == 60):
        return "El==e"
    elif (id == 28):
        return "Evelynn"
    elif (id == 81): 
        return "Ezreal"
    elif (id == 9):
        return "Fiddlesticks"
    elif (id == 114):
        return "Fiora"
    elif (id == 105):
        return "Fizz"
    elif (id == 3):
        return "Galio"
    elif (id == 41):
        return "Gangplank"
    elif (id == 86):
        return "Garen"
    elif (id == 150):
        return "Gnar"
    elif (id == 79):
        return "Gragas"
    elif (id == 104):
        return "Graves"
    elif (id == 887):
        return "Gwen"
    elif (id == 120):
        return "Hecarim"
    elif (id == 74):
        return "Heimerdinger"
    elif (id == 420):
        return "Illaoi"
    elif (id == 39):
        return "Irelia"
    elif (id == 427):
        return "Ivern"
    elif (id == 40):
        return "Janna"
    elif (id == 59):
        return "JarvanIV"
    elif (id == 24):
        return "Jax"
    elif (id == 126):
        return "Jayce"
    elif (id == 202):
        return "Jhin"
    elif (id == 222):
        return "Jinx"
    elif (id == 145):
        return "Ka==a"
    elif (id == 429):
        return "Kal==ta"
    elif (id == 43):
        return "Karma"
    elif (id == 30):
        return "Karthus"
    elif (id == 38):
        return "Kassadin"
    elif (id == 55):
        return "Katarina"
    elif (id == 10):
        return "Kayle"
    elif (id == 141):
        return "Kayn"
    elif (id == 85):
        return "Kennen"
    elif (id == 121):
        return "Khazix"
    elif (id == 203):
        return "Kindred"
    elif (id == 240):
        return "Kled"
    elif (id == 96):
        return "KogMaw"
    elif (id == 7):
        return "Leblanc"
    elif (id == 64):
        return "LeeSin"
    elif (id == 89):
        return "Leona"
    elif (id == 876):
        return "Lillia"
    elif (id == 127):
        return "L==sandra"
    elif (id == 236):
        return "Lucian"
    elif (id == 117):
        return "Lulu"
    elif (id == 99):
        return "Lux"
    elif (id == 54):
        return "Malphite"
    elif (id == 90):
        return "Malzahar"
    elif (id == 57):
        return "Maokai"
    elif (id == 11):
        return "MasterYi"
    elif (id == 21):
        return "M==sFortune"
    elif (id == 62):
        return "MonkeyKing"
    elif (id == 82):
        return "Mordeka==er"
    elif (id == 25):
        return "Morgana"
    elif (id == 267):
        return "Nami"
    elif (id == 75):
        return "Nasus"
    elif (id == 111):
        return "Nautilus"
    elif (id == 518):
        return "Neeko"
    elif (id == 76):
        return "Nidalee"
    elif (id == 56):
        return "Nocturne"
    elif (id == 20):
        return "Nunu"
    elif (id == 2): 
        return "Olaf"
    elif (id == 61):
        return "Orianna"
    elif (id == 516):
        return "Ornn"
    elif (id == 80):
        return "Pantheon"
    elif (id == 78):
        return "Poppy"
    elif (id == 555):
        return "Pyke"
    elif (id == 246):
        return "Qiyana"
    elif (id == 133):
        return "Quinn"
    elif (id == 497):
        return "Rakan"
    elif (id == 33):
        return "Rammus"
    elif (id == 421):
        return "RekSai"
    elif (id == 526):
        return "Rell"
    elif (id == 58):
        return "Renekton"
    elif (id == 107):
        return "Rengar"
    elif (id == 92):
        return "Riven"
    elif (id == 68):
        return "Rumble"
    elif (id == 13):
        return "Ryze"
    elif (id == 360):
        return "Samira"
    elif (id == 113):
        return "Sejuani"
    elif (id == 235):
        return "Senna"
    elif (id == 147):
        return "Seraphine"
    elif (id == 875):
        return "Sett"
    elif (id == 35):
        return "Shaco"
    elif (id == 98):
        return "Shen"
    elif (id == 102):
        return "Shyvana"
    elif (id == 27):
        return "Singed"
    elif (id == 14):
        return "Sion"
    elif (id == 15):
        return "Sivir"
    elif (id == 72):
        return "Skarner"
    elif (id == 37):
        return "Sona"
    elif (id == 16):
        return "Soraka"
    elif (id == 50):
        return "Swain"
    elif (id == 517):
        return "Sylas"
    elif (id == 134):
        return "Syndra"
    elif (id == 223):
        return "TahmKench"
    elif (id == 163):
        return "Taliyah"
    elif (id == 91):
        return "Talon"
    elif (id == 44):
        return "Taric"
    elif (id == 17):
        return "Teemo"
    elif (id == 412):
        return "Thresh"
    elif (id == 18):
        return "Tr==tana"
    elif (id == 48):
        return "Trundle"
    elif (id == 23):
        return "Tryndamere"
    elif (id == 4):
        return "Tw==tedFate"
    elif (id == 29):
        return "Twitch"
    elif (id == 77):
        return "Udyr"
    elif (id == 6):
        return "Urgot"
    elif (id == 110):
        return "Varus"
    elif (id == 67):
        return "Vayne"
    elif (id == 45):
        return "Veigar"
    elif (id == 161):
        return "Velkoz"
    elif (id == 711):
        return "Vex"
    elif (id == 254):
        return "Vi"
    elif (id == 234):
        return "Viego"
    elif (id == 112):
        return "Viktor"
    elif (id == 8):
        return "Vladimir"
    elif (id == 106):
        return "Volibear"
    elif (id == 19):
        return "Warwick"
    elif (id == 498):
        return "Xayah"
    elif (id == 101):
        return "Xerath"
    elif (id == 5):
        return "XinZhao"
    elif (id == 157):
        return "Yasuo"
    elif (id == 777):
        return "Yone"
    elif (id == 83):
        return "Yorick"
    elif (id == 350):
        return "Yuumi"
    elif (id == 154):
        return "Zac"
    elif (id == 238):
        return "Zed"
    elif (id == 115):
        return "Ziggs"
    elif (id == 26):
        return "Zilean"
    elif (id == 142):
        return "Zoe"
    elif (id == 143):
        return "Zyra"


