"""
Title: Egge_usersp2.py
Written by: William Egge
Date: 2023-04-29
Description: This module creates a new user document, displays the newly created user document, updates the email address of the previously created user document, displays the updated user document, deletes the previously created user document, and proves the document was deleted.

"""

# Import the MongoClient class
from pymongo import MongoClient

# Connect to the MongoDB server and get the database
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.up6klva.mongodb.net/web335DB?retryWrites=true&w=majority")

# Get the database
db = client['web335DB']

# Get the 'users' collection
users_collection = db['users']

# Write the Python code to create a new user document.
def create_user(first_name, last_name, email):
    new_user = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }
    user_id = users_collection.insert_one(new_user).inserted_id
    return user_id

user_id = create_user("John", "Doe", "john.doe@example.com")
print("User created with ID:", user_id)


# Write the Python code to display the newly created user document
def find_user_by_id(user_id):
    user = users_collection.find_one({"_id": user_id})
    return user

print("Newly created user:", find_user_by_id(user_id))


# Write the Python code to update the email address of the previously created user document
def update_user_email(user_id, new_email):
    users_collection.update_one({"_id": user_id}, {"$set": {"email": new_email}})

new_email = "johndoe_updated@example.com"
update_user_email(user_id, new_email)
print("Email updated")


# Write the Python code to display the updated user document
print("Updated user:", find_user_by_id(user_id))


# Write the Python code to delete the previously created user document
def delete_user(user_id):
    users_collection.delete_one({"_id": user_id})

delete_user(user_id)
print("User deleted")

#Write the Python code to prove the document was deleted
deleted_user = find_user_by_id(user_id)
if deleted_user:
    print("User still exists:", deleted_user)
else:
    print("User not found, successfully deleted")


# Close the connection
client.close()