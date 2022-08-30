from pymongo import MongoClient
from abc import ABC
from bclib.db_manager.db import Db
from bclib.db_manager.mongo_db import MongoDb

class Db(ABC):
    """Base class for implement data base interface"""

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def get_db():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Manzoomeh_shopping"]
    return db

def clean_data(data):
    pass 

def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/myFirstDatabase"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['user_shopping_list']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()

collection_name = dbname["user_1_items"]
item_1 = {
"_id" : "U1IT00001",
"item_name" : "Blender",
"max_discount" : "10%",
"batch_number" : "RR450020FRG",
"price" : 340,
"category" : "kitchen appliance"
}

item_2 = {
"_id" : "U1IT00002",
"item_name" : "Egg",
"category" : "food",
"quantity" : 12,
"price" : 36,
"item_description" : "brown country eggs"
}
collection_name.insert_many([item_1,item_2])
print (collection_name)

def get_db_logs():
    logs_address = ""
    client = MongoClient("mongodb://localhost:27017/")
    db = client["logs_daily"]    
    for log_address in logs_address:
        client = MongoClient(log_address)
        
