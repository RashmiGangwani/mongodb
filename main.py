import pymongo
import certifi
client = pymongo.MongoClient("mongodb://rashmi:12345@ac-boqpqol-shard-00-00.hmmlux9.mongodb.net:27017,ac-boqpqol-shard-00-01.hmmlux9.mongodb.net:27017,ac-boqpqol-shard-00-02.hmmlux9.mongodb.net:27017/?ssl=true&replicaSet=atlas-xyhkb5-shard-0&authSource=admin&retryWrites=true&w=majority",tlsCAFile=certifi.where())
db = client.test

data={
    "name" : "rashmi",
    "mail_id" : "rashmi@gmail.com",
    "subject" : ["data science", "data analytics", "big data"]

}
list_of_records=[
    {
        "companyname" : "iNeuron",
        "product" : 'Affordable AI',
        "courseOffered" : 'Machine Learning with Deployment'
    },
    {
        "companyname": "iNeuron",
        "product": 'Affordable AI',
        "courseOffered": 'Deep Learning for NLP and CV'
    },
    {
        "companyname": "iNeuron",
        "product": 'Master Programme',
        "courseOffered": 'Data Science Master Programme'
    }
]

database = client["myinfo"]
collection = database["rashmi"]

#collection.insert_one(data)

#collection.insert_many(list_of_records)

data1 = {"packetType":"D","data":{"checkEngineLightFlag":"F","batteryVoltageStableTime":0,"batteryVoltageStable":"0","batteryVoltageOff":"12.42","batteryCrankParamTN":"-0.08","batteryCrankParamVN":"0.00","batteryCrankParamTP":"-0.08","batteryCrankParamVP":"0.00","batteryCrankParamTT":"-0.00008","batteryCrankParamV0":"0.00","batteryVoltageMaxOn":"13.05","batteryVoltageMinOn":"12.97","batteryVoltageMaxOff":"12.46","batteryVoltageMinOff":"12.36","batteryVoltageOnAverage":"13.02","engineLoadMax":"84","engineLoadAverage":"39.98","rpmMax":"3487","rpmAverage":"1431.29","gpsSpeedAverage":"21.99","vssMax":"53.44","vssAverage":"23.06","tcuTemperatureMin":"82.40","tcuTemperatureMax":"109.40","tcuTemperatureAverage":"104.87","coolantMin":"158.00","coolantMax":"188.60","coolantAverage":"180.20","packetStartLocal":1508143346000,"tripStartLocal":1508143346000,"milIndicator":"F","monitorsNotReady":0,"imei":"60DF5417","gatewayTs":1515613306592,"diagnosticTroubleCodeData":[345345],"diagnosticPidData":[[64768,47,100],[64768,1,517376],[64800,1,262144],[64768,5,125]]},"header":{"iwrapVer":"1.9.20","sourceSystem":"CDP","configVer":"1.1","oemName":"HUM","unitType":0,"cpVer":"7.50.1.9","igpsVer":"1.3.7","messageType":"Notification","pomVer":"1.0","headerVer":"V6","timestamp":0,"deviceType":"InDrive","visorVer":"1.4.35","transactionId":"53098471-7787-4160-94b3-cd69dcc70416","deviceSerialNo":"60DF5417","subOrganization":"HUM","organization":"HUM","imei":"60DF5417","operation":"Notification"}}

#collection.insert_one(data1)

collection1= database["dpkt"]

#collection1.insert_one(data1)

