import json

f = open('diesel.json',)
  
price = json.load(f)
  
for i in price:
    if i["rate"] <= '50' :
     print(i)
  
f.close()