import pymongo
import certifi
client = pymongo.MongoClient("mongodb://rashmi:12345@ac-boqpqol-shard-00-00.hmmlux9.mongodb.net:27017,ac-boqpqol-shard-00-01.hmmlux9.mongodb.net:27017,ac-boqpqol-shard-00-02.hmmlux9.mongodb.net:27017/?ssl=true&replicaSet=atlas-xyhkb5-shard-0&authSource=admin&retryWrites=true&w=majority",tlsCAFile=certifi.where())
db = client.test

database=client['inventory']
collection = database['table']

data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]

#collection.insert_many(data)

#d = collection.find()
#d = collection.find({'status':'A'})
#d = collection.find({'status':{'$in':['A','D']}})
#d = collection.find({'status':{'$gt':'C'}})
#d = collection.find({'qty':{'$gte':100}})
#d = collection.find({'qty':{'$gte':75}})
#d = collection.find({ 'item': 'sketch pad' , 'qty': 95 })
#d = collection.find({ 'item': 'sketch pad' , 'qty': {'$gte': 75}}) #bydefault and condition
#d = collection.find({'$or' : [{'item': 'sketch pad'} , {'qty': {'$gte': 75}}]})
#collection.update_one({"item":'canvas'} , {'$set': {'item' : 'sheet'}})
collection.delete_one({"item":'sheet'})

d = collection.find()
for i in d:
    print(i)