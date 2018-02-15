import pymongo

connection = pymongo.MongoClient("149.89.150.100")
db = connection.test
collection = db.restaurants

def find_borough(b):
    name = []
    all = collection.find( {"borough": b} )
    for each in all:
        name.append(each)
    return name

def find_zpcode(z):
    info = []
    all = collection.find( {"address.zipcode": z} )
    for each in all:
        info.append(each)
    return info

def find_zpc_grade(z, g):
    info = []
    all = collection.find( {"address.zipcode": z}, {"grades.grade": g} )
    for each in all:
        one = collection.find_one({"_id" : each["_id"]})
        info.append(one)
    return info

def find_zpc_score(z, g):
    info = []
    all = collection.find( {"address.zipcode": z}, {"grades.score": g} )
    for each in all:
        one = collection.find_one({"_id" : each["_id"]})
        info.append(one)
    return name


i = 0
while i < 10:
    print find_zpc_grade("11225", "A")[i]['name']
    print find_zpc_grade("11225", "A")[i]['zipcode']
    print find_zpc_grade("11225", "A")[i]['grades']['grade']
    print "      "
    i = i + 1
