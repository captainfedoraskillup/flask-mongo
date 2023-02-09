from pymongo import MongoClient

# docker run -d --name mongodb-test -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME= -e MONGO_INITDB_ROOT_PASSWORD= -e MONGO_INITDB_DATABASE=collection mongo

def init_db():
    client = MongoClient('mongodb://%s:%s@127.0.0.1' % ('', ''))
    client.tododb.todo.delete_many({})
    client.tododb.todo.insert_many(
        [
            {"priority": "high",
            "title": "Get milk"},
            {"priority": "medium",
            "title": "Get gasoline"},
            {"priority": "low",
            "title": "Water plants"}
        ]
    )
    return client