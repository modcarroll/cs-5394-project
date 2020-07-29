## CS 5394 Project

`python3 main.py` to run.

### API

The API will have the following endpoints:

---

POST `https://pycontrolapi.us-south.cf.appdomain.cloud/logs`

/* Post an object to the logs collection */

Example input:

{"user": "morgan", "device": "lightbulb","action":"turn-on"}

---
POST `https://pycontrolapi.us-south.cf.appdomain.cloud/deviceon/:id`

/* Turn on a device by id where :id is the id of the device ("lightbulb", "doorlock", etc.) */

Example input:

{"deviceId":"lightbulb"}

---
POST `https://pycontrolapi.us-south.cf.appdomain.cloud/deviceoff/:id`

/* Turn off a device by id where :id is the id of the device ("lightbulb", "doorlock", etc.) */

Example input:

{"deviceId":"lightbulb"}

---
GET `https://pycontrolapi.us-south.cf.appdomain.cloud/devicestatus/:id`

/* Get the status of a device */

No input

---
GET `https://pycontrolapi.us-south.cf.appdomain.cloud/user/:id`

/* Get user information for a specific user where :id is the username */

No input

---
GET `https://pycontrolapi.us-south.cf.appdomain.cloud/allusers`

/* Get a list of all users */

No input
