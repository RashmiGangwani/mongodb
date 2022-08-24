import pymongo
import certifi
client = pymongo.MongoClient("mongodb://rashmi:12345@ac-xyefa1c-shard-00-00.ihbycfj.mongodb.net:27017,ac-xyefa1c-shard-00-01.ihbycfj.mongodb.net:27017,ac-xyefa1c-shard-00-02.ihbycfj.mongodb.net:27017/?ssl=true&replicaSet=atlas-1bt5hn-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

data={
    "name" : "rashmi",
    "mail_id" : "rashmi@gmail.com",
    "subject" : ["data science", "data analytics", "big data"]

}

database = client["myinfo"]
collection = database["rashmi"]
collection.insert_one(data)