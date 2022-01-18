# LOL-BestChampPick
a combination between python-flask, that fetch data and send from league client during champion select thanks to LCU and compare picked champs to the gamesDataBase that we need to collect using my other python script and then send the games result to localhost:5000/members that will be read by electron-reactJS script to present the results as a GUI on browser (localhost:5000)

***

## How to run
### To start collecting games data: 
Before running the script make sure you have updated the code with an active API key provided by RIOT on their developers pages. Update the following lines in the code.
```python
KEY = 'YOUR API KEY'
```
Once the machine is ready with all the packages required and the script is updated with a new api key, run the script using the following command. The file requires a region index for choosing the region to gather LoL game statistics from.

Region keys are as follows:
- North America = 0
- Brazil = 1
- Europe and Nordic Region = 2
- Europe West = 3
- Japan = 4
- Latin America South = 5
- Latin Americal North = 6
- Oceanic = 7
- Russia = 8
- Turkey = 9
- Korea = 10
<br/>
The following command will start gathering data from the Europe West.

$ cd project_directory/
$ python data_gathering_riot.py 3

to run the code, all data will be saved to json files take a look at [the original github/code](https://github.com/shrinivasshetty21/Data-Mining-from-RIOT-API) for more info and how does it exactly work. (was broken, so i fixed it BUT BEWARE I TESTED ONLY FOR EUROPE WEST, YOU NEED TO CHANGE PLAYER NAMES OF OTHER REAGION TO GET A BETTER STARTING POINT)

___
### To run the LCU and Python-flask script:
 
```
python connector.py
```
___
### To run the Electron-ReactJS script:

```
cd client
npm start
```
