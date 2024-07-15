from flask import Flask,jsonify
from markupsafe import escape
from app.CreateDatabases import CreateDB
from flask import render_template
#http://127.0.0.1:5000/prices/6762810635
app = Flask(__name__)

@app.route("/specs/<int:id>",methods=['GET'])
def GetSpecs(id):
    query = f'SELECT * FROM ATable WHERE "id"=={id}'
    dbObj=CreateDB()
    df=dbObj.ReadDb(query,"HousesSpecsDb.db").reset_index(drop=True)
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
if __name__ == '__main__':
    app.run(port=5004,debug=True)
