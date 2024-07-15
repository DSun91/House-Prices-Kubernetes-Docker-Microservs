from flask import Flask,jsonify
from markupsafe import escape
from app.CreateDatabases import CreateDB
from flask import render_template

#http://127.0.0.1:5000/prices/6762810635

app = Flask(__name__)

@app.route("/geoloc/<int:id>",methods=['GET'])
def GetGeoLoc(id):
    query = f'SELECT * FROM ATable WHERE "id"=={id}'
    dbObj=CreateDB()
    df=dbObj.ReadDb(query,"HousesDbGeoLoc.db").reset_index(drop=True)
    data = {
        'postalCode': str(df["Postal Code"][0]),
        'lattitude': str(df["Lattitude"][0]),
        'longitude': str(df["Longitude"][0])
    }

    return jsonify(data)
if __name__ == '__main__':
    app.run(port=5001,debug=True)