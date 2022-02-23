from flask import Flask, Response, request
from dotenv import load_dotenv
import json
import pymongo
import os
from bson.objectid import ObjectId

load_dotenv()
app = Flask(__name__)


conn_string = {os.getenv("CONNECTION_STRING")}

# set a 5-second connection timeout
client = pymongo.MongoClient(
    conn_string,
    serverSelectionTimeoutMS=5000
)
try:
    db = client.company
    print(client.server_info())
except Exception:
    print("Cannot connect to DB.")


@app.route('/users', methods=['POST'])
def create_user():
    try:
        user = {
            "name": request.form["name"],
            "lastname": request.form["lastname"]
        }
        dbResponse = db.users.insert_one(user)

        #for attr in dir(dbResponse):
        #   print(attr)
        print(dbResponse.inserted_id)
        return Response(
            response= json.dumps({
                "message" : "user created",
                "id" : f"{dbResponse.inserted_id}"
            }),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)

@app.route('/users', methods=['GET'])
def get_all_users():
    try:
        users = list(db.users.find())
        for user in users:
            user["_id"] = str(user["_id"])
        return Response(
            response= json.dumps(users),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({
                "message" : "cannot read users",
            }),
            status=500,
            mimetype="application/json"
        )
   


if __name__ == "__main__":
    app.run(debug=True)