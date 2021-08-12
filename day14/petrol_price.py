import json
file = open('petrol.json',)  
price = json.load(file) 
li = [i for i in price if i['rate']<'70']
print(li) 
file.close()