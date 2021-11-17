from flask import Flask
import logging
from datetime import datetime

app = Flask(__name__)

logging.basicConfig(filename="app.log", level=logging.DEBUG , format="%(message)s")


def log(endpoint):
    logging.debug("{}, {} endpoint was reached".format(datetime.now(), endpoint))
        


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/status")
def status():    
    log("status")
    return { "result": "OK - healthy" }


@app.route("/metrics")
def metrics():    
    log("metrics")
    return { "data": {"UserCount": 140, "UserCountActive": 23} }



if __name__ == "__main__":
    app.run(host='0.0.0.0')
