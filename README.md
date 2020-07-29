## CS 5394 Project

`python3 main.py` to run.

### API

The API will have the following endpoints:

---

POST /logs

/* Post an object to the logs collection */

Example input:

{"user": "morgan", "device": "lightbulb","action":"turn-on"}

---
POST /deviceon/:id

/* Turn on a device by id where :id is the id of the device ("lightbulb", "doorlock", etc.) */

Example input:

{"deviceId":"lightbulb"}

---
POST /deviceoff/:id

/* Turn off a device by id where :id is the id of the device ("lightbulb", "doorlock", etc.) */

Example input:

{"deviceId":"lightbulb"}

---
GET /devicestatus/:id

/* Get the status of a device */

No input

---
GET /user/:id

/* Get user information for a specific user where :id is the username */

No input

---
GET /allusers

/* Get a list of all users */

No input
