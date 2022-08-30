import pymongo
import certifi
client = pymongo.MongoClient("mongodb://rashmi:12345@ac-boqpqol-shard-00-00.hmmlux9.mongodb.net:27017,ac-boqpqol-shard-00-01.hmmlux9.mongodb.net:27017,ac-boqpqol-shard-00-02.hmmlux9.mongodb.net:27017/?ssl=true&replicaSet=atlas-xyhkb5-shard-0&authSource=admin&retryWrites=true&w=majority",tlsCAFile=certifi.where())
db = client.test

database = client["myinfo"]
collection = database["rashmi"]

'''record = collection.find()
for i in record:
    print(i)

d1 = collection.find({"companyname" : "iNeuron"})
for i in d1:
    print(i)
'''

d2= collection.find({'courseOffered':{'$gt':'E'}})
for i in d2:
    print(i)