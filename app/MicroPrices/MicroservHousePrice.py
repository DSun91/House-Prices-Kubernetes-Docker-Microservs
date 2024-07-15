from flask import Flask,jsonify
from markupsafe import escape
from app.CreateDatabases import CreateDB
from flask import render_template
#http://127.0.0.1:5000/prices/6762810635
app = Flask(__name__)

@app.route("/prices/<int:id>",methods=['GET'])
def GetPrice(id):
    query = f'SELECT * FROM ATable WHERE "id"=={id}'
    dbObj=CreateDB()
    df=dbObj.ReadDb(query,"HousesDbPrice.db").reset_index(drop=True)
    data = {
        'price': str(df["Price"][0])
    }
    return jsonify(data)

import json
@app.route("/prices",methods=['GET'])
def GetPricesList():
    query = f'SELECT * FROM ATable'
    dbObj=CreateDB()
    df=dbObj.ReadDb(query,"HousesDbPrice.db").reset_index(drop=True)
    df.applymap(str)
    records = df.to_dict(orient='records')

    # Convert list of dictionaries to a JSON string
    json_result = json.dumps(records, indent=4)

    return json_result


if __name__ == '__main__':
    app.run(port=5003,debug=True)