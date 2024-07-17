from flask import Flask,jsonify
from markupsafe import escape
from flask import render_template
import pandas as pd
import sqlite3
import logging
from logging.handlers import RotatingFileHandler
#http://127.0.0.1:5000/prices/6762810635
app = Flask(__name__)

def ReadDb(query, DbName):
    # Step 1: Connect to the SQLite database
    conn = sqlite3.connect(DbName)  # Replace with your database name
    cursor = conn.cursor()

    cursor.execute(query)
    rows = cursor.fetchall()

    # Step 4: Get column names
    column_names = [description[0] for description in cursor.description]

    # Step 5: Convert the results into a pandas DataFrame (optional)
    df = pd.DataFrame(rows, columns=column_names)

    df = df.reset_index(drop=True)
    # Step 6: Close the connection
    conn.close()

    # Print the DataFrame to see the data
    return df
@app.route("/prices/<int:id>",methods=['GET'])
def GetPrice(id):
    query = f'SELECT * FROM ATable WHERE "id"=={id}'

    df=ReadDb(query,"./MicroPrices/HousesDbPrice.db").reset_index(drop=True)
    data = {
        'price': str(df["Price"][0])
    }
    return jsonify(data)

import json
@app.route("/prices",methods=['GET'])
def GetPricesList():
    query = f'SELECT * FROM ATable'

    df= ReadDb(query,"./MicroPrices/HousesDbPrice.db").reset_index(drop=True)
    df.applymap(str)
    records = df.to_dict(orient='records')

    # Convert list of dictionaries to a JSON string
    json_result = json.dumps(records, indent=4)

    return json_result



# if __name__ == '__main__':
#     app.run(port=5003,debug=True)