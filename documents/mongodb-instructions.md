Install mongodb: [https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/](https://docs.mongodb.com/manual/mongo/#start-the-mongo-shell-and-connect-to-mongodb)

Using mongo shell: [https://docs.mongodb.com/manual/mongo/#start-the-mongo-shell-and-connect-to-mongodb](https://docs.mongodb.com/manual/mongo/#start-the-mongo-shell-and-connect-to-mongodb)

Pymongo is what we will use for our app: [https://pymongo.readthedocs.io/en/stable/](https://pymongo.readthedocs.io/en/stable/)

Run server: `brew services start/stop mongodb-community@4.2`

Login to the mongo shell: `mongo`

Show database: `show dbs`

Switch to test database: `use test` (Note: you should see 

Show collections: `show collections`

Insert data: `db.testCollection.insertOne( {
user: "morgan",
object: "bulb",
action: "turn-on",
timestamp: "20200722152128"
} );`

You should get a response that says something along the lines of:
`{
	"acknowledged" : true,
	"insertedId" : ObjectId("5f18a75bde25859e3c18687b")
}`

Show all items in the collection: `db.testCollection.find().pretty()`

To exit: `exit`

Stop all mongo instances: `sudo killall mongod`


