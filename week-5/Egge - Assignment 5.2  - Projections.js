/**
	Title: Egge – Assignment 5.2  – Projections.js
    Author: William Egge
    Date: 14 April 2023
    Description: Add a new user to the users collection, update Mozart’s email address, and list all users in the users collection.
 */

// Write a query to add a new user to the users collection.
newUser = {
  firstName: "New",
  lastName: "User",
  employeeId: "1013",
  email: "nuser@me.com",
  dateCreated: new Date(),
};

db.users.insertOne(newUser);

// Write a query to update Mozart’s email address
db.users.updateOne(
  { email: "wmozart@me.com" },
  { $set: { email: "mozart@me.com" } }
);

// Write a query to update prove that the update was successful
db.users.find(
  { firstName: "Wolfgang", lastName: "Mozart" },
  { _id: 0, firstName: 1, lastName: 1, email: 1 }
);

// List all users in the users collection
// Display only the firstName, lastName, and email fields
db.users.find({}, { _id: 0, firstName: 1, lastName: 1, email: 1 });
