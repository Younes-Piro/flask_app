import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

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
