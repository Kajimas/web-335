"""
Title: Egge_usersp1.py
Written by: William Egge
Description:
Date: 2023-04-23

This module contains several functions that perform various tasks.

"""


from pymongo import MongoClient

# Replace the placeholder values with your actual connection details
MONGODB_HOST = "your_host"
MONGODB_PORT = your_port
MONGODB_USERNAME = "your_username"
MONGODB_PASSWORD = "your_password"
MONGODB_DB_NAME = "web335DB"

# Connection string (URI) for MongoDB
connection_uri = f"mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}/{MONGODB_DB_NAME}?authSource=admin"

# Connect to the MongoDB server and get the database
client = MongoClient(connection_uri)
db = client['web335DB']

# Get the 'users' collection
users_collection = db['users']

# Display all documents in the 'users' collection
print("All documents in the 'users' collection:")
for document in users_collection.find():
    print(document)

# Display the document where the employeeId is 1011
print("\nDocument with employeeId 1011:")
document_employeeId = users_collection.find_one({'employeeId': 1011})
print(document_employeeId)

# Display the document where the lastName is Mozart
print("\nDocument with lastName Mozart:")
document_lastName = users_collection.find_one({'lastName': 'Mozart'})
print(document_lastName)

# Close the connection
client.close()
