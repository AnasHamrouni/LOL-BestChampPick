""" This module is used to get League of Legends match data using
    RIOT API from North America region."""
# Loading dependencies.
import time
from datetime import datetime
import os
from os import listdir, getcwd
from os.path import isfile, join
import sys
import json
import requests


# API key and loading file name.
KEY            = 'RGAPI-77f51a79-b2cf-4a32-8dc6-4a7cd4e92043'
SLEEPTIME      = 1.2
LOLDATA        = "lol_match_data"
GAMEDATA       = "Game_Stats"
MATCHID        = "Match_ID"
UNUSEDACCOUNTS = "Unused_Account_ID"
USEDACCOUNTS   = "Used_Account_ID"
OUTPUT_FOLDER  = "Output"
# Stores the output to a file.

def store_data(lol_match_data, game_stats, account_id_list, summoner_id, match_id_json, region):
    """ This function is used to store files. """
    data_file           = "{0}_{1}.json".format(LOLDATA, region)
    game_data_file      = "{0}_{1}.json".format(GAMEDATA, region)
    unused_account_file = "{0}_{1}.json".format(UNUSEDACCOUNTS, region)
    used_account_file   = "{0}_{1}.json".format(USEDACCOUNTS, region)
    matchid_file        = "{0}_{1}.json".format(MATCHID, region)

    with open(data_file, "w",encoding='utf-8') as file_name:
        json.dump(lol_match_data, file_name)

    with open(game_data_file, 'w',encoding='utf-8') as file_name:
        json.dump(game_stats, file_name)

    with open(used_account_file, 'w',encoding='utf-8') as file_name:
        json.dump(account_id_list, file_name)

    with open(unused_account_file, 'w',encoding='utf-8') as file_name:
        json.dump(summoner_id, file_name)

    with open(matchid_file, 'w',encoding='utf-8') as file_name:
        json.dump(match_id_json, file_name)
# Gets the current datetime formatted for output.
def get_date_string():
    """ This function is used to get date as string. """
    return "[{0}]".format(str((datetime.now())))

# Prefix for regular printouts.
def pre_print(region):
    """ This function is used to get date and region as string. """
    return "{0} [{1}]".format(get_date_string(), region)

# Prefix for error printouts.
def pre_print_err(region):
    """ This function is used to print error. """
    return "{0} #### ERROR ####".format(pre_print(region))

def region_selector(region_idx):
    """ This function is used to select the region for gathering LoL data. """
    if region_idx == 0:
        region   = 'na1'
        summoner = 'RiotSchmick'
        gregion = 'americas'

    elif region_idx == 1:
        region   = 'br1'
        summoner = 'Damage'
        gregion = 'americas'
        
    elif region_idx == 2:
        region   = 'eun1'
        summoner = 'Erring'
        gregion = 'europe'

    elif region_idx == 3:
        region   = 'euw1'
        summoner = 'BurnsTaichou'
        gregion = 'europe'

    elif region_idx == 4:
        region   = 'jp1'
        summoner = 'GaengMoyashi'
        gregion = 'asia'
        
    elif region_idx == 5:
        region   = 'la2'
        summoner = 'Josedeodo'
        gregion = 'americas'
        
    elif region_idx == 6:
        region   = 'la1'
        summoner = 'Seranok'
        gregion = 'americas'
        
    elif region_idx == 7:
        region   = 'oc1'
        summoner = 'Destinyy'
        gregion = 'asia'
        
    elif region_idx == 8:
        region   = 'ru'
        summoner = 'Seliorz'
        gregion = 'europe'
        
    elif region_idx == 9:
        region   = 'tr1'
        summoner = 'StarScreen'
        gregion = 'europe'
        
    elif region_idx == 10:
        region   = 'kr'
        summoner = 'junGsanGhyuN1'
        gregion = 'asia'
        
    else:
        region   = None
        summoner = None
        gregion = None
    return region, summoner, gregion

def get_account_id_list_v2(riot_key, region_idx):
    """ This functions gets League of Legends match data from RIOT API. """
    start_time = time.time()
    region, summoner,gregion = region_selector(region_idx)
    print('{0} Starting Data Gathering!'.format(pre_print(region)))

    if summoner is None or region is None:
        print("{0} Invalid Summoner or Region Name!".format(pre_print_err(region)))
        exit(1)

    # Declaring API addresses.
    api_key           = '?api_key={0}'.format(riot_key)
    match_list_api    = 'https://{0}.api.riotgames.com/lol/match/v5/matches/by-puuid/'.format(
        gregion)
    match_data_api    = 'https://{0}.api.riotgames.com/lol/match/v5/matches/'.format(
        gregion)
    summoner_info_api = 'https://{0}.api.riotgames.com/lol/summoner/v4/summoners/by-name/'.format(
        region)

    # Loading data stored by the program in earlier runs.
    file_path           = getcwd()
    files               = [x for x in listdir(file_path) if isfile(join(file_path, x))]
    lol_match_data      = {}
    data_file           = "{0}_{1}.json".format(LOLDATA, region)
    game_data_file      = "{0}_{1}.json".format(GAMEDATA, region)
    unused_account_file = "{0}_{1}.json".format(UNUSEDACCOUNTS, region)
    used_account_file   = "{0}_{1}.json".format(USEDACCOUNTS, region)
    matchid_file        = "{0}_{1}.json".format(MATCHID, region)

    current_data_count = 0

    # Loading LoL match data
    file_name = [x for x in files if data_file in x]
    if len(file_name) >= 1:
        print('{0} Pulling data from RIOT api ...'.format(pre_print(region)))
        print('{0} Loading LoL match data.'.format(pre_print(region)))
        with open(data_file, "r") as f_name:
            lol_match_data = json.load(f_name)
        print('{0} Loading {1} complete.'.format(pre_print(region), file_name[0]))

    else:
        print('{0} Pulling Data From: {1} With Summoner ID: {2}...'.format(
            pre_print(region),
            region,
            summoner))
        with open(data_file, "w",encoding='utf-8') as f_name:
            json.dump(lol_match_data, f_name)

    # Loading account id already used to access match data.
    file_name = [x for x in files if used_account_file in x]
    if len(file_name) >= 1:
        print('{0} Loading account ids already used for data gathering.'.format(pre_print(region)))
        with open(used_account_file, "r") as f_name:
            account_id_list = json.load(f_name)
        print('{0} Loading {1} complete.'.format(pre_print(region), file_name[0]))
    else:
        account_id_list = []

    # Loading project related data.
    file_name = [x for x in files if game_data_file in x]
    if len(file_name) >= 1:
        print('{0} Loading project related data.'.format(pre_print(region)))
        with open(game_data_file, "r") as f_name:
            game_stats = json.load(f_name)
        print('{0} Loading {1} complete.'.format(pre_print(region), file_name[0]))
    else:
        game_stats = []

    # Loading match ids.
    file_name = [x for x in files if matchid_file in x]
    if len(file_name) >= 1:
        print('{0} Loading match ids.'.format(pre_print(region)))
        with open(matchid_file, "r") as f_name:
            match_id_json = json.load(f_name)
        print('{0} Loading {1} complete.'.format(pre_print(region), file_name[0]))
    else:
        match_id_json = []

    # Loading account ids used for accessing match data.
    file_name = [x for x in files if unused_account_file in x]
    if len(file_name) >= 1:
        print('{0} Loading account ids yet to be used for data gathering.'
              .format(pre_print(region)))
        with open(unused_account_file, "rb") as f_name:
            summoner_id = json.load(f_name)
        print('{0} Loading {1} complete.'.format(pre_print(region), file_name[0]))

    else:
        url = "{0}{1}{2}".format(summoner_info_api, summoner, api_key)
        summoner_req = requests.get(url)
        time.sleep(SLEEPTIME)
        summoner_info = json.loads(summoner_req.text)
        summoner_id = [summoner_info['puuid']]

    # Variable used for preventing data from being stored at the first run.
    # Declaring variables for storing game statistics.
    temp_stats = []

    while len(summoner_id) >= 1:
        # Removing the account id from the list after accessing data.
        summoner_id_new = summoner_id.pop(0)
        # Avoiding duplicate summoner ids.
        if summoner_id_new not in account_id_list:
            # Obtaining latest 100 matches played by this account.
            url = "{0}{1}/ids{2}&startTime=1641510000&type=ranked&count=100".format(match_list_api, summoner_id_new, api_key)
            print("{0} Getting Account Matches.".format(pre_print(region)))
            account_info = None
            try:
                account_info = requests.get(url)
            except requests.ConnectionError:
                summoner_id.append(summoner_id_new)
            except Exception as error:
                print("{0} Requesting Data for Account: {1} : {2}".format(pre_print_err(region),
                                                                          summoner_id_new,
                                                                          error))
                continue
            time.sleep(SLEEPTIME)

            if account_info is not None and account_info.status_code == 200:
                print('{0}     Data from account: {1}'.format(pre_print(region), summoner_id_new))
                matches = json.loads(account_info.text)
                game_id_list = [v for v in matches]
                print("{0}         Matches Found: {1} : {2}".format(pre_print(region),
                                                                    len(game_id_list),
                                                                    current_data_count))
                
                for match_id_new in game_id_list:
                    # Selecting unique matches for getting match data.
                    # print("HERE")
                    if match_id_new not in match_id_json:
                        match_id_json.append(match_id_new)
                        # Obtaining match data for the respective match id.
                        url = "{0}{1}{2}".format(match_data_api, match_id_new, api_key)
                        
                        print("{0}             Requesting: {1}".format(pre_print(region),
                                                                       match_id_new))
                        match_data = None
                        try:
                            match_data = requests.get(url)
                            
                        except Exception as error:
                            print("{0} Requesting Data for Match ID: {1}:{2}"
                                  .format(pre_print_err(region), match_id_new, error))

                        time.sleep(SLEEPTIME)

                        if match_data is not None and match_data.status_code == 200:
                            match_json = json.loads(match_data.text)
                            #print(match_json)
                            lol_match_data[match_id_new] = match_json
                            current_data_count += 1
                            game_info = [int(match_json['info']['mapId'])] + [int(match_json['info']['queueId'])]
                            game_info += [str(match_json['info']['gameMode'])] + [(match_id_new)]

                            for match in match_json['info']['participants']:
                                if len(match_json['info']['participants']) == 10:
                                    try:
                                        temp_stats.append(match['championId'])
                                    except KeyError:
                                        temp_stats.append('NA')
                                    try:
                                        temp_stats.append(match['teamPosition'])
                                    except KeyError:
                                        temp_stats.append('NA')
                                    try:
                                        temp_stats.append(match['teamId'])
                                    except KeyError:
                                        temp_stats.append('NA')

                                    temp_stats = temp_stats + game_info

                                    if isinstance(match['win'], bool) is True:
                                        if match['win']:
                                            temp_stats.append(1)
                                        else:
                                            temp_stats.append(0)
                                    else:
                                        temp_stats.append(match['win'])
                                game_stats.append(temp_stats)
                                temp_stats = []

                            # Getting account ids for all the players in the match.
                            try:
                                match_data_player = match_json['metadata']['participants']
                                temp_id = [ v for v in match_data_player]
                                summoner_id += temp_id
                                temp_id = []
                            except KeyError:
                                pass

                        elif match_data is not None:
                            status = match_data.status_code
                            message = None
                            try: # Make sure the message exists
                                status_json = match_data.json()
                                msg_json = status_json['status']
                                message = msg_json['message']
                            except KeyError:
                                pass
                            print("{0} Failed to Get Data From Account: {1} "
                                  "Match ID: {2} "
                                  "Message: {3}".format(pre_print_err(region),
                                                        summoner_id_new,
                                                        match_id_new,
                                                        message))

                            if status == 429:
                                for j in range(120, 0, -1):
                                    time.sleep(1)
                                    print("\r{0}s ".format(j), end="")
                                    sys.stdout.flush()
                                sys.stdout.flush()
                            elif status == 503:
                                message = None
                                try: # Make sure the message exists
                                    status_json = match_data.json()
                                    msg_json = status_json['status']
                                    message = msg_json['message']
                                except KeyError:
                                    pass
                                print("{0} Error in Account ID: {1} Message: {2}".format(
                                    pre_print_err(region),
                                    summoner_id_new,
                                    message))

                            elif status == 403:
                                message = None
                                try: # Make sure the message exists
                                    status_json = match_data.json()
                                    msg_json = status_json['status']
                                    message = msg_json['message']
                                except KeyError:
                                    pass
                                print("{0} Error in Account ID: {1} Message: {2}".format(
                                    pre_print_err(region),
                                    summoner_id_new,
                                    message))

                                print('{0} Storing information about games before exitting.'
                                      .format(pre_print(region)))

                                store_data(lol_match_data, game_stats, account_id_list, summoner_id, match_id_json, region)

                                print("{0} Data Stored, Exitting ...".format(pre_print(region)))
                                return
                            else:
                                message = None
                                try: # Make sure the message exists
                                    status_json = match_data.json()
                                    msg_json = status_json['status']
                                    message = msg_json['message']
                                except KeyError:
                                    pass
                                print("{0} Error in Account ID: {1} Message: {2}".format(
                                    pre_print_err(region),
                                    summoner_id_new,
                                    message))

                        else:
                            print("{0} Requesting Match Data Failed! Waiting..."
                                  .format(pre_print_err))
                            for j in range(10, 0, -1):
                                time.sleep(1)
                                print("\r{0}s ".format(j), end="")
                                sys.stdout.flush()
                            sys.stdout.flush()

                    # Storing data gathered from the API.
                    if current_data_count >= 1000:
                        print('{0} Storing information about 1000 games.'.format(pre_print(region)))
                        print("{0} Script Runtime --- {1} Minutes ---".format(
                            pre_print(region),
                            (time.time() - start_time)/60))
                        start_time = time.time()

                        store_data(lol_match_data, game_stats, account_id_list, summoner_id, match_id_json, region)

                        current_data_count = 0
                        print("{0} Data Stored!!".format(pre_print(region)))

                    # Switch files if it excedes 1GB
                    if os.stat(data_file).st_size >= 1000000000:
                        overflowfile = "./{0}/{1}_{2}_{3}.json".format(OUTPUT_FOLDER,
                                                                       LOLDATA,
                                                                       region,
                                                                       time.time())

                        with open(data_file, "w",encoding='utf-8') as file_name:
                            json.dump(lol_match_data, file_name)
                        os.rename(data_file, overflowfile)
                        print("{0} File Size Exceded! Storing the data in different file.".format(
                            pre_print(region)))

                        lol_match_data = {} # Initiate with empty data
                        with open(data_file, "w",encoding='utf-8') as file_name:
                            json.dump(lol_match_data, file_name)
                        print('{0} Creating an empty file.'.format(pre_print(region)))

                account_id_list.append(summoner_id_new)

            elif account_info is not None:
                status = account_info.status_code
                print('{0} API failed to return account data with status code: {1}'.format(
                    pre_print_err(region),
                    status))

                if status == 429:
                    for j in range(120, 0, -1):
                        time.sleep(1)
                        print("\r{0}s ".format(j), end="")
                        sys.stdout.flush()
                    sys.stdout.flush()
                elif status == 503:
                    message = None
                    try: # Make sure the message exists
                        status_json = account_info.json()
                        msg_json = status_json['status']
                        message = msg_json['message']
                    except KeyError:
                        pass

                    print("{0} Error in Account ID: {1} Message: {2}".format(
                        pre_print_err(region),
                        summoner_id_new,
                        message))

                elif status == 403:
                    message = None
                    try: # Make sure the message exists
                        status_json = account_info.json()
                        msg_json = status_json['status']
                        message = msg_json['message']
                    except KeyError:
                        pass

                    print("{0} Error in Account ID: {1} Message: {2}".format(
                        pre_print_err(region),
                        summoner_id_new,
                        message))
                    print('{0} Storing information about games before exitting.'
                          .format(pre_print(region)))

                    store_data(lol_match_data, game_stats, account_id_list, summoner_id, match_id_json, region)
                    return

                else:
                    message = None
                    try: # Make sure the message exists
                        status_json = account_info.json()
                        msg_json = status_json['status']
                        message = msg_json['message']

                        print("{0} Error in Account ID: {1} Message: {2}".format(
                            pre_print_err(region),
                            summoner_id_new,
                            message))
                    except KeyError:
                        pass


            else:
                print("{0} Requesting Account Data Failed! Waiting...".format(pre_print_err))

                for j in range(10, 0, -1):
                    time.sleep(1)
                    print("\r{0}s ".format(j), end="")
                    sys.stdout.flush()
                sys.stdout.flush()

#### MAIN ####
def main():
    """ Main Function used to call other functions and run the program."""
    # Region Keys are as follows:
    # North America = 0
    # Brazil = 1
    # Europe and Nordic Region = 2
    # Europe West = 3
    # Japan = 4
    # Latin America South = 5
    # Latin Americal North = 6
    # Oceanic = 7
    # Russia = 8
    # Turkey = 9
    # Korea = 10

    get_account_id_list_v2(KEY, int(sys.argv[1]))

if __name__ == "__main__":
    main()
