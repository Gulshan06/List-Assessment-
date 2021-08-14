import smtplib,time,logging,pymongo
import validate as vegi
client = pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase= client['VegitableDb']
Collection_name =mydatabase['vegitables']

try:
    print("**@@@@@@ VEGITABLE SHOP @@@@@@**")
    vegitable_list=[]
    class VegitableDetails:
        def addvegidetails(self,vegitable_name,price,packing_date,expiry_date):
            current_time=time.strftime("%m-%d-%Y %H:%M:%S",time.localtime())
            dict1={"vegitable_name":vegitable_name,"price":price,"packing_date":packing_date,"expirydate":expiry_date,'AddOn':current_time}
            vegitable_list.append(dict1)
    obj1=VegitableDetails()
    while(True):
        print("1.Add Vegitables :-")
        print("2.View all vegitables details :-")
        print("3.Customer Details :-")
        print("4.List all the vegitable that expired today :-")
        print("5.Search the vegitable by name :-")
        print("6.Delete the vegitable by name :-")
        print("7.Update the vegitable by name :-")
        print("8.Exit :-")
        choice=int(input("enter your choice:"))
        if choice==1:
            vegitable_name=input("enter the vegitable name - ")
            price=input("enter the price of vegitable  - ")
            packing_date=input("enter vegitable packaging date in mm-dd-yyyy format - ")
            expiry_date=input("enter the expiry date in mm-dd-yyyy format - ")
            obj1.addvegidetails(vegitable_name,vegi.val_price(price),packing_date,expiry_date)
            result = Collection_name.insert_many(vegitable_list)
            print(result.inserted_ids)
        elif(choice==2):
            result = Collection_name.find()
            l=[]
            for i in result:
                l.append(i)
            print(l) 

        elif(choice==3):
            name= input("enter your name :-")
            emailid = input('enter your emailid :-')
            result=Collection_name.find()
            total_vegitable = []
            final_total=0
            for i in result:
                print('vegitable name - ',i['vegitable_name'] ,' price of vegitable - ',i['price'])
                x = int(input('enter the number of packet that you want (if you do noy want the product press 0)  -  '))
                total = i['price']*x
                final_total += total 
                if x > 0:
                    total_vegitable.append(i["vegitable_name"])
                    total_vegitable.append(i['price'])
                    total_vegitable.append(x)
            print('customer name - ',vegi.val_name(name))
            print('customer emailid - ',vegi.val_emailid(emailid))
            print(total_vegitable)
            print('your total amount is - ', final_total)
 
            connection=smtplib.SMTP("smtp.gmail.com",587)
            connection.starttls()
            connection.login("vaishnavi.p6521@gmail.com","Priy@6521")
            message='your total bill is - '+str(final_total)
            connection.sendmail("vaishnavi.p6521@gmail.com",emailid, message)
            print("Bill sended successful")
            connection.quit() 
        elif(choice == 4):
            print("list all the vegitables that expire today - ")
            current_date=time.strftime("%m-%d-%Y-",time.localtime())
            result=
            expired=(list(filter(lambda i:i["expirydate"]==str(current_date),vegitable_list)))    
            if len(expired)>0:
                print(expired)
            else:
                print("No Expired vegitable found")
        elif(choice == 5):
            # I=input("enter the vegitable that you want to search - ")
            # print(list(filter(lambda i:i["vegitablename"]==I,vegitable_list))) 
            x = input('enter the vegitable name :-')
            result = Collection_name.find({"vegitable_name":x})
            l = []
            for i in result:
                l.append(i)
            print(l) 

        elif(choice==6):
            y = input('enter the vegitable code :-')
            result=Collection_name.delete_one({'vegitable_name':y})
            print(result.deleted_count)

        elif(choice==7):
            result=Collection_name.update_one({'vegitable_price':40},{"$set":{"vegitable_name":'Onion'}})
        elif(choice==8):
            break

except Exception:
    logging.error("Something went wrong")
else:
    print("Your program completed Successfully")
finally:
    print("Thank You!!")















# import smtplib,time,logging
# import validate as vegi
# try:
#     print("**@@@@@@  VEGITABLE SHOP  @@@@@@ **")
#     vegitable_list=[]
#     class VegitableDetails:
#         def addvegidetails(self,vegitable_name,price,packing_date,expiry_date):
#             current_time=time.strftime("%m-%d-%Y %H:%M:%S",time.localtime())
#             dict1={"vegitable_name":vegitable_name,"price":price,"packing_date":packing_date,"expirydate":expiry_date,'AddOn':current_time}
#             vegitable_list.append(dict1)
#     obj1=VegitableDetails()
#     while(True):
#         print("1.Add Vegitables :-")
#         print("2.View all vegitables details :-")
#         print("3.Customer Details :-")
#         print("4.List all the vegitable that expired today :-")
#         print("5.Search the vegitable by name :-")
#         print("6.Exit :-")
#         choice=int(input("enter your choice:"))
#         if choice==1:
#             vegitable_name=input("enter the vegitable name - ")
#             price=input("enter the price of vegitable  - ")
#             packing_date=input("enter vegitable manufacturing date in mm-dd-yyyy format - ")
#             expiry_date=input("enter the expiry date in mm-dd-yyyy format - ")
#             obj1.addvegidetails(vegitable_name,vegi.val_price(price),packing_date,expiry_date)
            
#         elif(choice==2):
#             print(vegitable_list)
             
#         elif(choice==3):
#             name= input("enter your name :-")
#             emailid = input('enter your emailid :-')
#             total_vegitable = []
#             final_total=0
#             for i in vegitable_list:
#                 print('vegitable name - ',i['vegitable_name'] ,' price of vegitable - ',i['price'])
#                 x = int(input('enter the number of packet that you want (0 if you don\'t want)  -  '))
#                 total = i['price']*x
#                 final_total += total 
#                 if x > 0:
#                     total_vegitable.append(i["vegitable_name"])
#                     total_vegitable.append(i['price'])
#                     total_vegitable.append(x)
#             print('customer name - ',name)
#             print('customer emailid - ',vegi.val_emailid(emailid))
#             print(total_vegitable)
#             print('your total amount is - ', final_total)
#             connection=smtplib.SMTP("smtp.gmail.com",587)
#             connection.starttls()
#             connection.login("vaishnavi.p6521@gmail.com","Priy@6521")
#             message='your total amount is - '+str(final_total)
#             connection.sendmail("vaishnavi.p6521@gmail.com",emailid, message)
#             print("Message sended successful")
#             connection.quit()
             
#         elif(choice == 4):
#             print("list all the vegitables that expire today - ")
#             current_date=time.strftime("%m-%d-%Y-",time.localtime())
#             expired=(list(filter(lambda i:i["expirydate"]==str(current_date),vegitable_list)))    
#             if len(expired)>0:
#                 print(expired)
#             else:
#                 print("No Expired vegitable found")

#         elif(choice == 5):
#             I=input("enter the vegitable that you want to search - ")
#             print(list(filter(lambda i:i["vegitablename"]==I,vegitable_list)))  

#         elif(choice==6):
#             break

# except Exception:
#     logging.error("Something went wrong")
# else:
#     print("Your program completed Successfully")
# finally:
#     print("Thank You!!")




















# import re,sys,json,smtplib
# try:
#     header=['name','rollno','admno','college','parentname','mobilenumber','emailid','sub1mark','sub2mark','sub3mark','sub4mark','sub5mark']
#     studentlist=[]
#     class Studentdetail:
#         def addStudent(self,ls):
#             self.name=ls[0]
#             self.rollno=ls[1]
#             self.admno=ls[2]
#             self.college=ls[3]
#             self.parentname=ls[4]
#             self.mobilenumber=ls[5]
#             self.emailid=ls[6]
#     class Marks(Studentdetail):
#         def mark (self,ls):
#             super().__init__(ls)
#             self.sub1mark=ls[7]
#             self.sub2mark=ls[8]
#             self.sub3mark=ls[9]
#             self.sub4mark=ls[10]
#             self.sub5mark=ls[11]
#         def addStudentdetail(self,name,rollno,admno,college,parentname,mobilenumber,emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
#             total=sub1mark+sub2mark+sub3mark+sub3mark+sub4mark+sub5mark
#             dict={"name":name,"rollno":rollno,"admno":admno,"college":college,"parentname":parentname,"mobilenumber":mobilenumber,"emailid":emailid,"sub1mak":sub1mark,"sub2mark":sub2mark,"sub3mark":sub3mark,"sub4mark":sub4mark,"sub5mark":sub5mark}
#             studentlist.append(dict)
#         def validation(name,rollno,admno,college,parentname,mobilenumber,emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
#             validation=re.match(r'([a-zA-Z])\D*([a-zA-Z])$',name)
#             validation1=re.match('^[1-9]',rollno)
#             validation2=re.match('^[1-9]',admno)
#             validation3=re.match(r'/([A-Z][^\s,.]+[.]?\s[(]?)(University|Institute|College)[^,\d](?=,|\d)/',college)
#             validation4=re.match(r'([a-zA-Z])\D*([a-zA-Z])$',parentname)
#             validation5=re.match("(0|91)?[7-9][0-9]{9}",mobilenumber)
#             validation6=re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',emailid)
#             validation7=re.match('^[0-3]{1}[0-9]{1}|40$',sub1mark)
#             validation8=re.match('^[0-3]{1}[0-9]{1}|40$',sub2mark)
#             validation9=re.match('^[0-3]{1}[0-9]{1}|40$',sub3mark)
#             validation10=re.match('^[0-3]{1}[0-9]{1}|40$',sub4mark)
#             validation11=re.match('^[0-3]{1}[0-9]{1}|40$',sub5mark)
#             if validation and validation1 and validation2 and validation3 and validation4 and validation5 and validation6 and validation7 and validation8 and validation9 and validation10 and validation11 and validation11:
#                 return [int(name),int(rollno),int(admno),int(college),int(parentname),int(mobilenumber),int(emailid),int(sub1mark),int(sub2mark),int(sub3mark),int(sub4mark),int(sub5mark)]
#             else:
#                 print("you had enter wrong input")
#                 sys.exit()
#         obj=Studentdetail()
#         while(True):
#             print("1. Add Students -")
#             print("2. Display student details Like API - ")
#             print("3. Search student by Rollno - ")
#             print("4. Ranking - ")
#             print("5. Exit - ")
#             choice=int(input("Enter your choice :"))
#             if choice==1:
#                 name = input("enter the name of student : ")
#                 rollno=input("enter the Rollno : ")
#                 admno=input('enter the admin no :  ')
#                 college=input("enter the college name : ")
#                 parentname=input("enter the parent name : ")
#                 mobilenumber=input("enter the mobile number: ")
#                 emailid=input("enter the email id : ")
#                 sub1mark=input("enter the subject1 mark: ")
#                 sub2mark=input("enter the subject2 mark: ")
#                 sub3mark=input("enter the subject3 mark: ")
#                 sub4mark=input("enter the subject4 mark: ")
#                 sub5mark=input("enter the subject5 mark: ")
#                 obj=Studentdetail(validation(name,rollno,admno,college,parentname,mobilenumber,emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark))
#             if choice==2:
#                 print(studentlist)
#                 myjson=json.dumps(studentlist)
#                 with open('json1.json','w',encoding='UTF-8') as f:
#                     f.write(myjson)
#             if choice==3:
#                 searchroll=int(input("Enter roll number to search :"))
#                 # print(list(filter(lambda i:i["rollnum"]==searchroll,studentlist)))
#                 data=(sorted(studentlist,key=lambda i:i["totalmarks"],reverse=True))
#                 print(data)
#                 jdata=json.dumps(data)
#                 with open("json2".json,"w+",encoding="utf-8") as fi:
#                     fi.write(jdata)        
#             if choice==4:
#                 for i in studentlist:
#                     if i['totalmarks']<100:
#                         message=str(i)
#                         print(message)
#                         connection=smtplib.SMTP("smtp.gmail.com",587)
#                         connection.starttls()
#                         connection.login("vaishnavi.p6521@gmail.com","Priy@6521")
#                         connection.sendmail("vaishnavi.p6521@gmail.com","vaishnavihajela6520@gmail.com",message)
#                         connection.quit
#                         print("Mail sent")
# except Exception:
#     print("Wrong input")
# finally:
#      print("Thank You!")


# import re,sys,json,smtplib
# # try:
# header=['total','name','rollno','admno','college','parentname','mobilenumber','emailid','sub1mark','sub2mark','sub3mark','sub4mark','sub5mark']
# studentlist=[]
# class Studentdetail:
#     def addStudent(self,name,rollno,admno,college,parentname,mobilenumber,emailid):
#         self.name=name
#         self.rollno=rollno
#         self.admno=admno
#         self.college=college
#         self.parentname=parentname
#         self.mobilenumber=mobilenumber
#         self.emailid=emailid
# class Marks(Studentdetail):
#     def mark (self,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
#         self.sub1mark=sub1mark
#         self.sub2mark=sub2mark
#         self.sub3mark=sub3mark
#         self.sub4mark=sub4mark
#         self.sub5mark=sub5mark
#     def addStudentdetail(self,total,name,rollno,admno,college,parentname,mobilenumber,emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
#         total=sub1mark+sub2mark+sub3mark+sub3mark+sub4mark+sub5mark
#         dict={"total":total,"name":name,"rollno":rollno,"admno":admno,"college":college,"parentname":parentname,"mobilenumber":mobilenumber,"emailid":emailid,"sub1mak":sub1mark,"sub2mark":sub2mark,"sub3mark":sub3mark,"sub4mark":sub4mark,"sub5mark":sub5mark}
#         studentlist.append(dict)
#     def validation(name,rollno,admno,college,parentname,mobilenumber,emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
#         validation=re.match(r'([a-zA-Z])\D*([a-zA-Z])$',name)
#         validation1=re.match('^[1-9]',rollno)
#         validation2=re.match('^[1-9]',admno)
#         validation3=re.match(r'/([A-Z][^\s,.]+[.]?\s[(]?)(University|Institute|College)[^,\d](?=,|\d)/',college)
#         validation4=re.match(r'([a-zA-Z])\D*([a-zA-Z])$',parentname)
#         validation5=re.match("(0|91)?[7-9][0-9]{9}",mobilenumber)
#         validation6=re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',emailid)
#         validation7=re.match('^[0-3]{1}[0-9]{1}|40$',sub1mark)
#         validation8=re.match('^[0-3]{1}[0-9]{1}|40$',sub2mark)
#         validation9=re.match('^[0-3]{1}[0-9]{1}|40$',sub3mark)
#         validation10=re.match('^[0-3]{1}[0-9]{1}|40$',sub4mark)
#         validation11=re.match('^[0-3]{1}[0-9]{1}|40$',sub5mark)
#         if validation:
#             return name
#         else:
#             print("you had enter wrong input")
        
#         if validation1:
#             return int(rollno)
#         else:
#             print("you had enter wrong input")
        
#         if validation2:
#             return int(admno)
#         else:
#             print("you had enter wrong input")
        
#         if validation3:
#             return college
#         else:
#             print("you had enter wrong input")
#         if validation4:
#             return parentname
#         else:
#             print("you had enter wrong input")
#         if validation5:
#             return int(mobilenumber)
#         else:
#             print("you had enter wrong input")
#         if validation6:
#             return emailid
#         else:
#             print("you had enter wrong input")

#         if validation7:
#             return int(sub1mark)
#         else:
#             print("you had enter wrong input")

#         if validation8:
#             return int(sub2mark)
#         else:
#             print("you had enter wrong input")

#         if validation9:
#             return int(sub3mark)
#         else:
#             print("you had enter wrong input")
            
#         if validation10:
#             return int(sub4mark)
#         else:
#             print("you had enter wrong input")
#         if validation11:
#             return int(sub5mark)
#         else:
#             print("you had enter wrong input")

#     obj=Studentdetail()
#     while(True):
#         print("1. Add Students -")
#         print("2. Display student details Like API - ")
#         print("3. Search student by Rollno - ")
#         print("4. Ranking - ")
#         print("5. Exit - ")
#         choice=int(input("Enter your choice :"))
#         if choice==1:
#             name = input("enter the name of student : ")
#             rollno=input("enter the Rollno : ")
#             admno=input('enter the admin no :  ')
#             college=input("enter the college name : ")
#             parentname=input("enter the parent name : ")
#             mobilenumber=input("enter the mobile number: ")
#             emailid=input("enter the email id : ")
#             sub1mark=input("enter the subject1 mark: ")
#             sub2mark=input("enter the subject2 mark: ")
#             sub3mark=input("enter the subject3 mark: ")
#             sub4mark=input("enter the subject4 mark: ")
#             sub5mark=input("enter the subject5 mark: ")
#             obj=Studentdetail(validation(name),validation(rollno),validation(admno),validation(college),validation(parentname),validation(mobilenumber),validation(emailid),validation(sub1mark),validation(sub2mark),validation(sub3mark),validation(sub4mark),validation(sub5mark))
#         if choice==2:
#             print(studentlist)
#             myjson=json.dumps(studentlist)
#             with open('json1.json','w',encoding='UTF-8') as f:
#                 f.write(myjson)
#         if choice==3:
#             searchroll=int(input("Enter roll number to search :"))
#             # print(list(filter(lambda i:i["rollnum"]==searchroll,studentlist)))
#             data=(sorted(studentlist,key=lambda i:i["totalmarks"],reverse=True))
#             print(data)
#             jdata=json.dumps(data)
#             with open("json2".json,"w+",encoding="utf-8") as fi:
#                 fi.write(jdata)        
#         if choice==4:
#             for i in studentlist:
#                 if i['totalmarks']<100:
#                     message=str(i)
#                     print(message)
#                     connection=smtplib.SMTP("smtp.gmail.com",587)
#                     connection.starttls()
#                     connection.login("vaishnavi.p6521@gmail.com","Priy@6521")
#                     connection.sendmail("vaishnavi.p6521@gmail.com","vaishnavihajela6520@gmail.com",message)
#                     connection.quit
#                     print("Mail sent")
#             # print(sorted(studentlist,key=lambda i:i["total"],reverse=True))
#         if choice==5:
#             break
# # except Exception:
# #     print("Wrong input")
# # finally:
# #     print("Thank You!")