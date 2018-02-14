import pymongo

connection = pymongo.MongoClient("149.89.150.100")
db = connection.test
collection = db.restaurants

def find_borough(b):
    name = []
    all = collection.find( {"borough": b} )
    for each in all:
        name.append(each["name"])
    return name

def find_zpcode(z):
    name = []
    all = collection.find( {"address.zipcode": z} )
    for each in all:
        name.append(each["name"])
    return name

def find_grade_zpc(z, g):
    name = []
    all = collection.find( {"address.zipcode": z}, {"grades.grade": g} )
    for each in all:
        print each


print find_grade_zpc("11225", "A")
