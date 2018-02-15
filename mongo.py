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
    return info

print "=========================================="
i = 0
print "This are the test case for find_borough"
while i < 10:
    print find_borough("Brooklyn")[i]["borough"]
    print "      "
    i = i + 1

print "=========================================="
i = 0
print "This are the test case for find_zpcode"
while i < 10:
    print find_zpcode("11225")[i]["address"]["zipcode"]
    print "      "
    i = i + 1

print "=========================================="
i = 0
print "This are the test case for find_zpc_grade"
while i < 10:
    print find_zpc_grade("11225", "A")[i]['name']
    print find_zpc_grade("11225", "A")[i]['address']['zipcode']
    x = 0
    while x < len(find_zpc_grade("11225", "A")[i]['grades']):
        print find_zpc_grade("11225", "A")[i]['grades'][x]['score']
        x = x + 1
    print "      "
    i = i + 1

print "=========================================="
i = 0
print "This are the test case for find_zpc_score"
while i < 10:
    print find_zpc_score("11225", "$lt 10")[i]['name']
    print find_zpc_score("11225", "$lt 10")[i]['address']['zipcode']
    x = 0
    print "      "
    i = i + 1
