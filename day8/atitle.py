import requests
import json # java serialize object notation 
data=requests.get("https://jsonplaceholder.typicode.com/posts")
edata=data.json()
p=[]
for i in edata:
    p.append(i["title"])
# print(p)    
li=[x for x in p if x[0] =='a' in x]
print(li)