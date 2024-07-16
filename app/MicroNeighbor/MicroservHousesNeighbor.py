from flask import Flask,jsonify
from markupsafe import escape
from flask import render_template
import pandas as pd
import sqlite3
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
@app.route("/neighbor/<int:id>",methods=['GET'])
def GetNeighborhood(id):
    query = f'SELECT * FROM ATable WHERE "id"=={id}'

    df= ReadDb(query,"HousesDbNeighbor.db").reset_index(drop=True)
    data = {
        'schools': str(df["No of schools nearby"][0]),
        'airportDist': str(df["Distance from the airport"][0])
    }
    return render_template("neighbour.html",data=data)
    return jsonify(data)
# if __name__ == '__main__':
#     app.run(port=5002,debug=True)