# LOL-BestChampPick
a combination between python-flask, that fetch data and send from league client during champion select thanks to LCU and compare picked champs to the gamesDataBase that we need to collect using my other python script and then send the games result to localhost:5000/members that will be read by electron-reactJS script to present the results as a GUI on browser (localhost:5000)

***

## How to run
###To start collecting games data: change "KEY" in data_gathering_riot.py to your API KEY.

´´´
python data_gathering_riot.py 
´´´
to run the code, all data will be saved to json files take a look at [the original github/code](https://github.com/shrinivasshetty21/Data-Mining-from-RIOT-API) for more info and how does it exactly work. (was broken, so i fixed it)
___
### To run the LCU and Python-flask script:
 
´´´
python connector.py
´´´
___
### To run the Electron-ReactJS script:

´´´
cd client
npm start
´´´
