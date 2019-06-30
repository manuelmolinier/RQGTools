#!flask/bin/python
import json
import dice
from flask import Flask, Response
from helloworld.flaskrun import flaskrun
from classes.npcmaker import npcmaker
from classes.npcdatabase import npcdatabase
application = Flask(__name__)

@application.route('/', methods=['GET'])
def get():
    database=npcdatabase()
    npcmakervar=npcmaker(database)
    npcmakervar.create()
    result="{"
    for stat in npcmakervar.stats:
        result+= stat + ":"+ str(npcmakervar.stats[stat]) +","
    result+="}"
    return Response(json.dumps({'result': result}), mimetype='application/json', status=200)

@application.route('/', methods=['POST'])
def post():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)

if __name__ == '__main__':
    flaskrun(application)
