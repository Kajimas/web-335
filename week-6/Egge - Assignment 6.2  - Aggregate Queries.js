/**
	Title: Egge – Assignment 6.2 - Aggregate Queries.js
    Author: William Egge
    Date: 23 April 2023
    Description: A record of the queries used in Assignment 6.2.
 */

// Import the collections from the houses.js file.
load("./houses.js");

// Query the houses collection and output the results.
db.houses.find();

// Query the students collection and output the results.
db.students.find();

// Insert a new document into the houses collection.
db.students.insertOne({
  firstName: "John",
  lastName: "Doe",
  studentId: "s1020",
  houseId: "h1007",
});

// Find the document that was just inserted.
db.students.findOne({ firstName: "John", lastName: "Doe" });

// Delete the document that was just inserted.
db.students.deleteOne({ firstName: "John", lastName: "Doe" });

// Find the document that was just deleted.
db.students.findOne({ firstName: "John", lastName: "Doe" });

// Query the students and look up the list of students by house.
db.students.aggregate([
  {
    $lookup: {
      from: "houses",
      localField: "houseId",
      foreignField: "houseId",
      as: "house",
    },
  },
]);

// Query the students with the same house founder using lookup and match.
db.students.aggregate([
  {
    $lookup: {
      from: "houses",
      localField: "houseId",
      foreignField: "houseId",
      as: "house",
    },
  },
  {
    $match: { "house.founder": "Godric Gryffindor" },
  },
]);

// Query the students with the same mascot using lookup and match.
db.students.aggregate([
  {
    $lookup: {
      from: "houses",
      localField: "houseId",
      foreignField: "houseId",
      as: "house",
    },
  },
  {
    $match: { "house.mascot": "Eagle" },
  },
]);
