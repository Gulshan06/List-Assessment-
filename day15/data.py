from typing import Collection
import pymongo
# Servername - localhost 
# Database - studentdb
# username - 
# password - 
client = pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase= client['StudentDb']
Collection_name =mydatabase['Students']

while(True):
    print("1.Add")
    print('2.View')
    print('3.aggregate search by each branch name')
    print("4.delete name")
    print("4. Soft delete")
    print("5.update ")
    print("6.Search by name ")
    print("6.Break")
    choice = int(input("enter ur choice "))
    if choice==1:
        name = input('enter your name - ')
        rollno = int(input('enter your rollno - '))
        college=input('enter your college name - ')
        branch= input("enter your branch - ")
        dic = {'name':name,"rollno":rollno,'college':college,'branch':branch,"delflag":0}
        print(dic)
        result = Collection_name.insert_one(dic)
        print(result.inserted_id)
    if choice == 2:
        result= Collection_name.find({'delflag': 0})
        for i in result:
            print(i)
    if choice==3:
        result= Collection_name.aggregate([{'$group':{'_id':"$branch","no_of_student":{'$sum':1}}}])
        for i in result:
            print(i)
    if choice ==4 :
        roll = int(input())
        Collection_name.update_one({"rollno":roll},{"$set": {'delflag':1}})

    if choice==6:
        result=



    if choice ==7 :
        break

    # result = collection_name.find({'$and': [{"rollno":rollno},{"name":name}]})