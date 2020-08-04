const express = require("express");
const bodyParser = require('body-parser');
var moment = require('moment');
const MongoClient = require("mongodb").MongoClient;
const CONNECTION_URL = "mongodb://somestuff"; // paste your MongoDB URI here
const DATABASE_NAME = 'prod';
const app = express();

/* Swagger Section */
const expressSwagger = require('express-swagger-generator')(app);
let options = {
    swaggerDefinition: {
        info: {
            description: 'A smart device simulator',
            title: 'Smart PyControl',
            version: '1.1.0',
        },
        host: 'pycontrolapi.us-south.cf.appdomain.cloud',
        basePath: '/',
        schemes: ['https']
    },
    basedir: __dirname,
    files: ['server.js']
};
expressSwagger(options)
/* End Swagger */

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

var port = 3000;
var router = express.Router();

app.listen(port, () => {
  console.log("API running on port " + port);
  MongoClient.connect(CONNECTION_URL, { useNewUrlParser: true, tlsCAFile: `${__dirname}/client.pem` }, (error, client) => {
        if(error) {
            throw error;
        }

        client.db().admin().listDatabases().then(dbs => {
      });

        database = client.db(DATABASE_NAME);
        console.log("Connected to `" + DATABASE_NAME + "`!");
    });
});

router.get('/', function(req, res) {
  res.json({ message: 'Welcome to the PySmart Control API!' });
});

/**
 * Create a new entry in the logs collection for each device action change
 * @route POST /logs
 * @group logs - Operations related to logging
 * @param {string} user.parameter.required - username - eg: morgan
 * @param {string} device.parameter.required - device name - eg: speaker
 * @param {string} action.parameter.required - device name - eg: turn-on
 * @returns {object} 200 - {"message": "Success!"}
 * @returns {Error}  default - Unexpected error
 */
 app.post("/logs", (req, res) => {
   let inputObject = {
     "user": req.body.user,
     "device": req.body.device,
     "action": req.body.action,
     "timestamp": moment().format()
   }

   collection = database.collection("logs", {readPreference:'secondaryPreferred'});
   collection.insertOne(inputObject, (error, result) => {
     if (error) throw error;
     res.send({"message": "Success!"});
   });
 });

 /**
  * Set the thermostat to a specific temperature
  * Example: `/settemp`
  * @route POST /settemp
  * @group devices - Operations related to devices
  * @param {int} temperature.parameter.required - temperature, e.g. 74
  * @returns {object} 200 - {"message": "Success!"}
  * @returns {Error}  default - Unexpected error
  */
 app.post("/settemp", (req, res) => {
   collection = database.collection("devices", {readPreference:'secondaryPreferred'});
   collection.updateOne({"deviceId": "thermostat"}, {$set: {temperature: req.body.temperature}}, (error, result) => {
     if (error) throw error;
     res.send({"message": "Success!"});
     });
   });

/**
* Set the volume to a specific value
* Example: `/setvolume`
* @route POST /setvolume
* @group devices - Operations related to devices
* @param {integer} volume.parameter.required - volume, e.g. 10
* @returns {object} 200 - {"message": "Success!"}
* @returns {Error}  default - Unexpected error
*/
app.post("/setvolume", (req, res) => {
 collection = database.collection("devices", {readPreference:'secondaryPreferred'});
 collection.updateOne({"deviceId": "speaker"}, {$set: {volume: req.body.volume}}, (error, result) => {
   if (error) throw error;
   res.send({"message": "Success!"});
   });
 });

 /**
  * Turn a device on by device ID where :id is the device ID
  * Example: `/deviceon/lightbulb`
  * @route POST /deviceon/:id
  * @group devices - Operations related to devices
  * @param {string} id.parameter.required - device ID - eg: lightbulb
  * @returns {object} 200 - {"message": "Success!"}
  * @returns {Error}  default - Unexpected error
  */
 app.post("/deviceon/:id", (req, res) => {
   collection = database.collection("devices", {readPreference:'secondaryPreferred'});
   collection.updateOne({"deviceId": req.params.id}, {$set: {status:"on"}}, (error, result) => {
     if (error) throw error;
     res.send({"message": "Success!"});
     });
   });

 /**
  * Turn a device off by device ID where :id is the device ID
  * Example: `/deviceoff/lightbulb`
  * @route POST /deviceoff/:id
  * @group devices - Operations related to devices
  * @param {string} id.parameter.required - device ID - eg: lightbulb
  * @returns {object} 200 - {"message": "Success!"}
  * @returns {Error}  default - Unexpected error
  */
 app.post("/deviceoff/:id", (req, res) => {
   collection = database.collection("devices", {readPreference:'secondaryPreferred'});
   collection.updateOne({"deviceId": req.params.id}, {$set: {status:"off"}}, (error, result) => {
       if (error) throw error;
       res.send({"message": "Success!"});
     });
   });

   /**
    * Turn a device volume/temperature up by device ID where :id is the device ID
    * Example: `/up/speaker`
    * @route POST /up/:id
    * @group devices - Operations related to devices
    * @param {string} id.parameter.required - device ID - eg: speaker
    * @returns {object} 200 - {"message": "Success!"}
    * @returns {Error}  default - Unexpected error
    */
   app.post("/up/:id", (req, res) => {
     collection = database.collection("devices", {readPreference:'secondaryPreferred'});

     if(req.params.id === 'thermostat') {
       collection.updateOne({"deviceId": req.params.id}, {$inc: {temperature: 1}}, (error, result) => {
           if (error) throw error;
           res.send({"message": "Success!"});
         });
     } else if (req.params.id === 'speaker') {
       collection.updateOne({"deviceId": req.params.id}, {$inc: {volume: 1}}, (error, result) => {
           if (error) throw error;
           res.send({"message": "Success!"});
         });
     } else {
       throw error;
     }
   });

 /**
  * Turn a device volume/temperature down by device ID where :id is the device ID
  * Example: `/down/speaker`
  * @route POST /down/:id
  * @group devices - Operations related to devices
  * @param {string} id.parameter.required - device ID - eg: speaker
  * @returns {object} 200 - {"message": "Success!"}
  * @returns {Error}  default - Unexpected error
  */
 app.post("/down/:id", (req, res) => {
   collection = database.collection("devices", {readPreference:'secondaryPreferred'});
   if(req.params.id === 'thermostat') {
     collection.updateOne({"deviceId": req.params.id}, {$inc: {temperature: -1}}, (error, result) => {
         if (error) throw error;
         res.send({"message": "Success!"});
       });
   } else if (req.params.id === 'speaker') {
     collection.updateOne({"deviceId": req.params.id}, {$inc: {volume: -1}}, (error, result) => {
         if (error) throw error;
         res.send({"message": "Success!"});
       });
   } else {
     throw error;
   }
   });

   /**
    * Get the status for a specific device
    * Example: `/devicestatus/speaker`
    * @route GET /devicestatus/:id
    * @group devices - Operations related to devices
    * @param {string} id.parameter.required - device ID - eg: speaker
    * @returns {object} 200 - {_id: String, deviceId: String, volume: int, status: String}
    * @returns {Error}  default - Unexpected error
    */
 app.get("/devicestatus/:id", (req, res) => {
   collection = database.collection("devices", {readPreference:'secondaryPreferred'});
   collection.findOne({"deviceId": req.params.id}, function(err, result) {
     if (err) throw err;
     console.log(result);
     res.send(result);
   });
 });

 /**
 * Get all logs
 * Example: `/alllogs`
 * @route GET /alllogs
 * @group logs - Operations related to logs
 * @returns {Array} 200 - [{_id: String, user: String, object: String, action: String, timestamp: String}]
 * @returns {Error}  default - Unexpected error
 */
 app.get("/alllogs", (req, res) => {
 collection = database.collection("logs", {readPreference:'secondaryPreferred'});
 collection.find({}).toArray(function(err, result) {
   if (err) throw err;
   console.log(result);
   res.send(result);
 });
 });

 /**
  * Get user information for a specific user
  * Example: `/user/morgan`
  * @route GET /user/:id
  * @group users - Operations related to users
  * @returns {object} 200 - {_id: String, userId: String, email: String}
  * @returns {Error}  default - Unexpected error
  */
 app.get("/user/:id", (req, res) => {
   collection = database.collection("users", {readPreference:'secondaryPreferred'});
   collection.findOne({"userId": req.params.id}, function(err, result) {
     if (err) throw err;
     console.log(result);
     res.send(result);
   });
 });

 /**
  * Get a list of users
  * @route GET /allusers
  * @group users - Operations related to users
  * @returns {Array} 200 - [{_id: String, userId: String, email: String}]
  * @returns {Error}  default - Unexpected error
  */
 app.get("/allusers", (req, res) => {
   collection = database.collection("users", {readPreference:'secondaryPreferred'});
   collection.find({}).toArray(function(err, result) {
     if (err) throw err;
     console.log(result);
     res.send(result);
   });
 });
