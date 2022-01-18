from flask import Flask
from lcu_driver import Connector
import GetChamps as GetChamps
from threading import Thread
import json
import sys

app = Flask(__name__)
connector = Connector()
games_data = GetChamps.get_champs()
data = []
# fired when LCU API is ready to be used
@connector.ready
async def connect(connection):
    print('LCU API is ready to be used.')


# fired when League Client is closed (or disconnected from websocket)
@connector.close
async def disconnect(_):
    print('The client have been closed!')
    await connector.stop()


# subscribe to '/lol-summoner/v1/current-summoner' endpoint for the UPDATE event
# when an update to the user happen (e.g. name change, profile icon change, level, ...) the function will be called
@connector.ws.register('/lol-summoner/v1/current-summoner', event_types=('UPDATE',))
async def icon_changed(connection, event):
    print(f'The summoner {event.data["displayName"]} was updated.')
    
@connector.ws.register('/lol-champ-select/v1/session', event_types=('UPDATE',))
async def selection(connection, event):
    myTeam,enemyTeam = GetChamps.get_selected_champ(event.data)
    result = GetChamps.best_pick(myTeam ,enemyTeam,games_data)
    global data
    data  = result
    sys.stdout.flush()

@app.route("/members")
def members():
    return json.dumps(data)
    #return {"members":["Member1","Member2","Member3"]}

def startconnector():
    connector.start()
if __name__ == "__main__":
    # starts the connector
    Thread(target = startconnector).start()
    app.run(debug=True)
    
    