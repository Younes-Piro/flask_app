from flask import Flask, Response, request
import json
from bson.objectid import ObjectId
from Models import User
from mongoengine import connect
from dotenv import load_dotenv
import os

load_dotenv()

conn_string = {os.getenv("CONNECTION_STRING")}
# set a 5-second connection timeout
try:
    connect(host= conn_string , alias='default')
except Exception as ex:
    print(ex)    


app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    try:
        user = User.User(
            name = request.form["name"],
            lastname = request.form["lastname"]
        )
        user.save()
        #for attr in dir(dbResponse):
        #   print(attr)
        return Response(
            response= json.dumps({
                "message" : "user created",
                "id" : f'{user.id}'
            }),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    app.run(debug=True)