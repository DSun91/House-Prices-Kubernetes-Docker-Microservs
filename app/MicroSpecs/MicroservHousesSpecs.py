from flask import Flask,jsonify
from markupsafe import escape
from flask import render_template
import pandas as pd
import sqlite3
import socket
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


@app.route("/", methods=['GET'])
def get_host_ip():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)

    data = {
        'hostname': hostname,
        'ip_address': host_ip
    }

    return jsonify(data)
@app.route("/specs/<int:id>",methods=['GET'])
def GetSpecs(id):
    query = f'SELECT * FROM ATable WHERE "id"=={id}'

    df= ReadDb(query,"./MicroSpecs/HousesSpecsDb.db").reset_index(drop=True)
    print(df.columns)
    data = {
        'date': str(df["Date"][0]),
        'bedrooms': str(df["No of bedrooms"][0]),
        'bathrooms': str(df["No of bathrooms"][0]),
        'livingArea': str(df["living area"][0]),
        'lotArea': str(df["lot area"][0]),
        'floors': str(df["No of floors"][0]),
        'waterfront': str(df["waterfront present"][0]),
        'conditions': str(df["house condition"][0]),
        'grade': str(df["house grade"][0]),
        'areaMinusBasement': str(df["house area(excluding basement)"][0]),
        'basement': str(df["Area of the basement"][0]),
        'buildYear': str(df["Built Year"][0]),
        'renovationArea': str(df["Renovation Year"][0]),
        'livingAreaRenov': str(df["living_area_renov"][0]),
        'lotAreaRenov': str(df["lot_area_renov"][0])
    }
    return render_template("house_specs.html",data=data)
    #return jsonify(data)
# if __name__ == '__main__':
#     app.run(port=5004,debug=True)
