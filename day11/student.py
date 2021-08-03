import sys
student= []
class StudentData:
    def addDetails(self,name,rollno,admin,english,hindi,maths,science,social):
        totalmarks=english+hindi+maths+science+social
        dict1 = {'total':totalmarks,'name':name,'rollno':rollno,'admin':admin,'english':english,'hindi':hindi,'maths':maths,'science':science,'social':social}
        student.append(dict1)
obj1=StudentData()
while(True):
    print("1. Add student details - ")
    print("2. Display student details Like API - ")
    print("3. Search student by Rollno - ")
    print("4. Ranking - ")
    print("5. Exit - ")
    choice = int(input())
    if choice==1:
        name = input("enter the name of student - ")
        rollno= int(input("enter the Rollno - "))
        admin = int(input('enter the admin no -  '))
        english=int(input("enter the english marks:"))
        maths=int(input("enter the maths marks:"))
        social=int(input("enter the social marks:"))
        hindi=int(input("enter the hindi marks:"))
        science=int(input("enter the science marks:"))
        obj1.addDetails(name,rollno,admin,english,hindi,maths,science,social)
    if choice==2:
        print(student)
    if choice==3:
        srollno = int(input('enter the rollno to search - '))
        print(list(filter(lambda i:i['rollno']==srollno,student)))
    if choice == 4:
        print(sorted(student,reverse=True,key=lambda i:i['total']))
    if choice==5:
        sys. exit()


