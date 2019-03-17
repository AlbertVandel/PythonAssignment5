import json
from flask import Flask, request
app = Flask(__name__)

SERVER_PASSWORD = 'ad'

@app.route('/', methods= ['GET','POST'])
def login():
    if request.method == 'POST':
        req = json.loads(request.get_json())
        if(req['password'] == SERVER_PASSWORD):
            return '', 200 
        else:
            return '', 403
    else:    
        return 'Hello, World!'