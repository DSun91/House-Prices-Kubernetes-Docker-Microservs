from flask import Flask,jsonify
from markupsafe import escape
from app.CreateDatabases import CreateDB
from flask import render_template

#http://127.0.0.1:5000/prices/6762810635

app = Flask(__name__)

@app.route("/neighbor/<int:id>",methods=['GET'])
def GetNeighborhood(id):
    query = f'SELECT * FROM ATable WHERE "id"=={id}'
    dbObj=CreateDB()
    df=dbObj.ReadDb(query,"HousesDbNeighbor.db").reset_index(drop=True)
    data = {
        'schools': str(df["No of schools nearby"][0]),
        'airportDist': str(df["Distance from the airport"][0])
    }

    return jsonify(data)
if __name__ == '__main__':
    app.run(port=5002,debug=True)