import collections
import re, time
print("Select an option from menu")
print("\n")
print("1. Add the student information ")
print("2. View student inforamation With RollNo ")
choice=int(input("enter the choice - "))
def addtimedate():
    time1=time.localtime()
    currenttime= time.strftime("%y-%m-%d  %H:%M:%S")
    return currenttime
li=[]
if(choice==1):
    a = int(input('Enter the no how many details you want to fill - '))
    for i in range(a):
        dict={}
        dict['name']= input('enter name of student - ')
        roll = input('enter rollno - ')
        val=re.search("^[1-9]",roll)
        if val:
            dict["rollno"]=int(roll)
        add=input("enter admission no")
        val1=re.search("^[1-9]",add)
        if val1:
            dict['admino']=int(add)
        dict['Maths'] =int(input("enter the mark of Maths : "))
        dict['Science']=int(input("enter the mark of science : "))
        dict['Hindi']=int(input("enter the mark of Hindi : "))
        dict['English']=int(input("enter the mark of English : "))
        dict['Social']=int(input("enter the mark of Social : "))
        dict['total']=dict['Maths']+dict['Science']+dict['Hindi']+dict['English']+dict['Social']
        dict["AddOn"]=addtimedate()
        li.append(dict)
if choice==2:
    def sal(li):   
            datawithrollno=[x for x in li if x['rollno'] in x]
            return datawithrollno
    print(li)
    marks=[]
    for i in li:
        marks.append(i['total'])
    print(sorted(marks))
else:
    print("Enter the wrong input")
        

# print(li)

# import collections
# import re
# print("Select an option from menu")
# print("\n")
# print("1.Add students detials:")
# print("2.search the students with roll no")
# print("3.list the student api with marks")
# print("4.print all the students")
# choice=int(input("enter the choice"))
# li=[]
# if(choice==1):
#     for i in range(3):
#         dict={}
#         print("add students details is selected")
#         dict["name"]=input("enter the studentname:")
#         dict["rollno"]=input("enter the roll no:")
#         dict["admission no"]=input("enter the admission no:")
# class Student():
#     def marks(self,m1,m2,m3,m4,m5):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#         self.m4=m4
#         self.m5=m5
#     def print(self):
        # print("enter the mark of Maths :",self.m1)
        # print("enter the mark of science :",self.m2)
        # print("enter the mark of Hindi :",self.m3)
        # print("enter the mark of English :",self.m4)
        # print("enter the mark of Social :",self.m5)
#     li.append(dict)
# print(li)
# if(choice==2):
#     print("Search the students with roll no is selected")
# def search(self,rollno):
#     for i in range(li._len_()):
#         if(li(i).rollno==5):
#             return i
# if(choice==3):
#     print("list the students api with marks")
#     for i in range(len(li)-1):
#             comb_dict=collections.ChainMap(li[i],li[i+1])
#             print(comb_dict)
# if(choice==4):
#     print("print all the students selected")
#     print(dict['studemts'])