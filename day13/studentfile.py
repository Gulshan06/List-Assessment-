import csv
header =['name','roll']

studentData=[
    {'name':'ram','roll':1},
    {'name':'rohit','roll':2},
    {'name':'ritik','roll':3},
    {'name':'roni','roll':4},
    {'name':'ramesh','roll':15},
    {'name':'ramu','roll':13}
]

with open('student.csv','w+',encoding='UTF8',newline='') as s:
    writer = csv.DictWriter(s,fieldnames=header)
    writer.writeheader()
    writer.writerows(studentData)