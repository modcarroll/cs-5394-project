### Data Format

Example:
```
{
   user: "morgan",
   device: "bulb",
   action: "turn-on",
   timestamp: "2020-07-22 21:09:14.288068"
}
```

Options for object key: ["lightbulb", "doorlock", "thermostat", "speaker"]

Options for action key: ["turn-on", "turn-off", "lock", "unlock", "turn-up", "turn-down"]

Note: We will not build anything in to enforce the integrity of these keys (unless we have time), so just make sure you follow this structure.

### Prerequisites

Install mongodb: [https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/](https://docs.mongodb.com/manual/mongo/#start-the-mongo-shell-and-connect-to-mongodb)

Using mongo shell: [https://docs.mongodb.com/manual/mongo/#start-the-mongo-shell-and-connect-to-mongodb](https://docs.mongodb.com/manual/mongo/#start-the-mongo-shell-and-connect-to-mongodb)

Pymongo is the package that we will use for our app to communciate with Mongo: [https://pymongo.readthedocs.io/en/stable/](https://pymongo.readthedocs.io/en/stable/)

Download the GUI for MongoDB here: [https://www.mongodb.com/try/download/compass](https://www.mongodb.com/try/download/compass)

### Connect to MongoDB - Cloud
Download the TLS Certificate (it is in the root directory of this repo)
Run `mongo -u $USERNAME -p $PASSWORD --ssl --sslCAFile 317d706c-6a8e-4ad4-89ef-7656d2ce97e8 --authenticationDatabase admin --host replset/08951464-2902-477e-862b-97095ae4d133-0.brjdfmfw09op3teml03g.databases.appdomain.cloud:32142,08951464-2902-477e-862b-97095ae4d133-1.brjdfmfw09op3teml03g.databases.appdomain.cloud:32142`
but replace `$USERNAME` with your username (your first name) and `$PASSWORD` with your password.

Mongo connection URI: `mongodb://admin:nAJENwqPxbC@08951464-2902-477e-862b-97095ae4d133-0.brjdfmfw09op3teml03g.databases.appdomain.cloud:32142?authSource=admin&replicaSet=replset&tls=true&readPreference=secondary`

### Run MongoDB Locally
Run server: `brew services start/stop mongodb-community@4.2`

Login to the mongo shell: `mongo`

Show database: `show dbs`

Switch to test database: `use test` (Note: you should see a few different databases, just use test)

Show collections: `show collections` (I see one collection here: testCollection)

Insert data: `db.testCollection.insertOne( {
user: "morgan",
object: "bulb",
action: "turn-on",
timestamp: "20200722152128"
} );`

^ `db` is the current database I have selected (test), `testCollection` is the collection name, and `insertOne()` is the method. The object that I want to insert is `{
user: "morgan",
object: "bulb",
action: "turn-on",
timestamp: "20200722152128"
}`

You should get a response that says something along the lines of:
`{
	"acknowledged" : true,
	"insertedId" : ObjectId("5f18a75bde25859e3c18687b")
}`

Show all items in the collection: `db.testCollection.find().pretty()`

To exit: `exit`

Stop all mongo instances: `sudo killall mongod`


