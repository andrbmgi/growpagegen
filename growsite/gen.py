import datetime
import requests
import json
import os
import sys
import logging
from time import sleep
import config

import pymongo


# Connect to the MongoDB database
def connect_db():
    username = config.username
    password = config.password
    auth_db = config.auth_db
    host = config.host
    port = config.port

    # Create the MongoDB client
    client = pymongo.MongoClient(f"mongodb://{username}:{password}@{host}:{port}/{auth_db}")

    # Access the specific database
    db = client[auth_db]

    # Access a specific collection
    collection = db[config.collection]
    return collection


# Find data in the MongoDB database
def find_data(collection, query):
    # Example: query = {"name": "weed"}
    # Find a document in the collection
    return collection.find_one(query)


collection = connect_db()
result = find_data(collection=collection, query={})
print(result)
# result: {'_id': ObjectId('6698478b61db402b45ed003f'), 'timestamp': '2024-07-18 00:36:59', 'topic': 'moisture', 'moist1': 12, 'perc1': 20, 'moist2': 4234, 'perc2': 30}
