from flask import Flask
from dotenv import load_dotenv
import pymongo
import os

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


@app.route('/')
def index():
    return "Hello"

if __name__ == "__main__":
    app.run(debug=True)