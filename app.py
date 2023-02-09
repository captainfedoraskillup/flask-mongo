from flask import Flask
from pymongo import MongoClient
from bson import json_util
import json

app = Flask(__name__)

from . import db
client = db.init_db()

@app.route("/todos")
def index():
    result = client.tododb.todo.find({})
    return json_util.dumps(result), 200

# @app.route("/todos/<priority>")
# def get_by_priority(priority):
#     result = client.tododb.todo.find({"priority": priority})
#     return json_util.dumps(result), 200

@app.route("/todos/<priority>")
def get_by_priority_better(priority):
    result = client.tododb.todo.find({"priority": priority})
    print(list(result))
    if not result or len(list(result)) < 1:
        return json_util.dumps(result), 404

    return json_util.dumps(result), 200

if __name__ == "__main__":
  app.run()