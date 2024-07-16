from flask import Flask,jsonify,request
from markupsafe import escape
from flask import render_template
import requests
import json
import pandas as pd
import socket
app = Flask(__name__)


PAGE_SIZE = 50
@app.route("/")
def main_page():
    #host_ip =  requests.get('http://housespecs:3000')
    # print(f"host ip hey la")
    # print(f"host ip {host_ip.content}")
    page = request.args.get('page', 1, type=int)
    #hs=json.loads(host_ip.content)
    # Calculate the start and end indices for pagination
    start_index = (page - 1) * PAGE_SIZE
    end_index = start_index + PAGE_SIZE

    # Fetch data from API
    api_response = requests.get('http://prices:5003/prices')

    if api_response.status_code == 200:
        house_prices = json.loads(api_response.content)
        total_count = len(house_prices)

        # Slice data for the current page
        paginated_prices = house_prices[start_index:end_index]

        # Calculate total pages
        total_pages = (total_count + PAGE_SIZE - 1) // PAGE_SIZE  # ceil(total_count / PAGE_SIZE)

        return render_template("index.html", adverts=paginated_prices, page=page, total_pages=total_pages)
    else:
        return f"<p>Error fetching data from API: {api_response.status_code} {api_response.content}</p>"


# if __name__ == '__main__':
#     app.run(port=5005,debug=True)