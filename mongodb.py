import pymongo
client = pymongo.MongoClient("mongodb+srv://mamta:Swapnil@mamta.mfuellw.mongodb.net/?retryWrites=true&w=majority")
db = client.test

d = {
    "name":"Swapnil",
    "email" : "swapnilrathod72@gmail.com",
    "surname" : "Rathod"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )
