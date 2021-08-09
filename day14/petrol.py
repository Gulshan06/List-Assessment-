import csv,json
myfile='C:/Users/gulsh/Desktop/Prodapt/Assessment/day14/petrol.csv'
jsonfilepath= "petrol.json"
li = []
with open(myfile,"r",encoding='utf-8') as f:
    datatreader=csv.DictReader(f)
    for i in datatreader:
        li.append(i)

petrol_li=json.dumps(li)
with open(jsonfilepath,'w',encoding='utf-8') as f:
    f.write(petrol_li)