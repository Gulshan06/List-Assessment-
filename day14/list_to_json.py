import json
Studentlist= [{'name':'rahul','age':22},{'name':'rahul','age':22},{'name':'rahul','age':22}]
myjson=json.dumps(Studentlist)
with open("test.json","w",encoding="utf-8") as f:
    f.write(myjson)
