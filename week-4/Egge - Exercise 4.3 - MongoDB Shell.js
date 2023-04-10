load("C:/Users/locke/OneDrive/Desktop/buwebdev/web-335/week-4/users.js")

db.users.find();

db.users.find({ email: "jbach@me.com" });

db.users.find({ lastName: "Mozart" });

db.users.find({ firstName: "Richard" });

db.users.find({ employeeId: "1010" });