from flask import Flask,jsonify
from markupsafe import escape
from app.CreateDatabases import CreateDB
from flask import render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def main_page():

    api_response_bytes = requests.get('http://127.0.0.1:5003/prices')

    if api_response_bytes.status_code==200:
        house_prices = json.loads(api_response_bytes.content)
        return render_template("index.html", adverts=house_prices)
    else:
        return "<p>House Prices Service Error!</p>"


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
#

if __name__ == '__main__':
    app.run(port=5005,debug=True)