### Data Format

Example:
```
{
   user: "morgan",
   object: "bulb",
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

### Run MongoDB
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


