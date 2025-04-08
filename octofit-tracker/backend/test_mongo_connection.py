from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def test_mongo_connection():
    try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']
        collections = db.list_collection_names()
        print("Successfully connected to MongoDB. Collections:", collections)
        try:
            # Test the connection
            client.admin.command('ping')
            print("MongoDB connection is active.")
        except ConnectionFailure as cf:
            print("MongoDB connection failed:", cf)
    except Exception as e:
        print("Error connecting to MongoDB:", e)

if __name__ == "__main__":
    test_mongo_connection()
