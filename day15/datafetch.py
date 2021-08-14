# crud = create retrieve/fetch update delete

# from day15.data import Collection_name

import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase = client['StudentDb']
Collection_name= mydatabase['Students']
result = Collection_name.find({},{"_id":0})
result = Collection_name.find()
# print(result)
for i in result:
    print(i)