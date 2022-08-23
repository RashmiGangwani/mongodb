import pymongo
client = pymongo.MongoClient("mongodb+srv://Rashmi:Asdfghjkl1@cluster0.twp3r1f.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name":"sudhanshu",
    "emailid": "sudhanshu@ineuron.ai",
    "surname": "kumar"
}

db1 = client['mongotest1']
coll = db1['test']
coll.insert_one(d)