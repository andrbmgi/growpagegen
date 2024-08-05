import datetime
import json
import os
import sys
import logging
from time import sleep
import config

import pymongo
import pandas as pd
from datetime import datetime


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
#result = find_data(collection=collection, query={})

# Fetch all data
data = list(collection.find({}))

# Convert MongoDB documents to JSON serializable format
for document in data:
    document["_id"] = str(document["_id"])
    document["timestamp"] = datetime.strptime(document["timestamp"], '%Y-%m-%d %H:%M:%S').isoformat()

# Create a DataFrame for easier manipulation
df = pd.DataFrame(data)
df['average_moist'] = (df['moist1'] + df['moist2']) / 2
df['smoothed_average_moist'] = df['average_moist'].rolling(window=5).mean()

# Fill NaN values in 'smoothed_average_moist' with 'average_moist'
df['smoothed_average_moist'].fillna(df['average_moist'], inplace=True)

# Convert DataFrame back to dictionary
data = df.to_dict(orient='records')

# Write data to JSON file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Data has been written to data.json")