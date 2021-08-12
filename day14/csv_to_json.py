import csv,json
myfile='C:/Users/gulsh/Desktop/Prodapt/Assessment/product.csv'
jsonfilepath= "student.json"
li = []
with open(myfile,"r",encoding='utf-8') as f:
    datatreader=csv.DictReader(f)
    for i in datatreader:
        li.append(i)
        # print(i)
    # print(datatreader)
student_li=json.dumps(li)
with open(jsonfilepath,'w',encoding='utf-8') as f:
    f.write(student_li)