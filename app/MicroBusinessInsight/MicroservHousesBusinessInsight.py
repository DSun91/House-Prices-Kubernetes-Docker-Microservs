from flask import Flask,jsonify
from markupsafe import escape
from app.CreateDatabases import CreateDB
from flask import render_template

#http://127.0.0.1:5000/prices/6762810635

app = Flask(__name__)

@app.route("/business/<int:id>",methods=['GET'])
def GetViews(id):
    query = f'SELECT * FROM ATable WHERE "id"=={id}'
    dbObj=CreateDB()
    df=dbObj.ReadDb(query,"HousesDbBusinessInsight.db").reset_index(drop=True)
    data = {
        'views': str(df["No of views"][0])

    }

    return jsonify(data)
# query = f'SELECT * FROM ATable WHERE "id"==6762810635'
# dbObj=CreateDB()
# df=dbObj.ReadDb(query,"HousesDbBusinessInsight.db").reset_index(drop=True)
# print(df)

if __name__ == '__main__':
    app.run(port=5000,debug=True)