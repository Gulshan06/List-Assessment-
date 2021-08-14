import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase = client['StudentDb']
Collection_name= mydatabase['Students']
# result = Collection_name.find({},{"_id":0})
# result = Collection_name.find({'name':{'$regex':"[^G]u$"}},{"_id":0})
# result = Collection_name.find({'name':{'$gt':"^G"}},{"_id":0})
# result = Collection_name.find({'name':{'$lt':"^r"}},{"_id":0})
result= Collection_name.delete_one({'name':"Gullu"})
result=Collection_name.update_one({'rollno':123},{"$set":{"name":'ram'}})
# for i in result:
#     print(i)
print("deleted")