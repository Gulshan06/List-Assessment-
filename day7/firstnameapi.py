import requests
import json # java serialize object notation 
data=requests.get("https://reqres.in/api/users?page=2")
edata=data.json()
# print(list(edata))
articles= edata["data"]
print(articles)
li =[] 
for i in articles:
    li.append(i["first_name"])
print(li)
print(*li)
