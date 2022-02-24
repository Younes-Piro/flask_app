from flask import Flask, Response, request
import json
from bson.objectid import ObjectId
from Models import User
from connection import db

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    try:
        users = User.User(request.form["name"],request.form["lastname"])
        user = users.create_user()
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