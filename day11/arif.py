import pymongo,logging,re,time,smtplib
client = pymongo.MongoClient("mongodb://localhost:27017/")

mydatabase= client["Mini1Db"]
Collection_name =mydatabase["minis1"]
Collection_name1=mydatabase["dish"]
clist=[]
menu=["dosa","idly","meat","Paneer","Roti"]
menudict=dict.fromkeys(menu,0)

class Customer:
    def addCustomer(self,name,mobileNumber,emailId,menudict):
        current_time=time.strftime("%m-%d-%Y %H:%M:%S",time.localtime())
        dict1={"name":name,"mobileNumber":mobileNumber,"emailId":emailId,"menudict":menudict,"AddOn":current_time}
        clist.append(dict1)
        #clist.append(menudict)
        print(clist)
k=Customer()
def validate(name,mobileNumber,emailId):
        name1=re.search("[A-Za-z]{0,25}$",name)
        print(name1)
        mobileNumber1=re.search("^(\+91)[6-9]\d{9}$",mobileNumber)
        print(mobileNumber1)
        emailId1=re.search( "[A-Za-z0-9]{0,20}@[a-z]+\.[a-z]{2,4}$",emailId)
        print(emailId1)   
        if name1 and  mobileNumber1 and emailId1:
            return True
        else:
            return False  

while(True):
    print("1.Add Customer")
    print("2. view Customer")
    print("3.search customer using name")
    print("4.delete customer")
    print("5.update customer")
    print("6.sent mail to customer")
    print("7.Exit")
    choice=int(input("Enter your choice :"))
    if choice==1:
        name = input("Enter the name of Customer:")
        mobileNumber=input("Enter the mobilenumber:")
        emailId=input("Enter the email:")
        if validate(name,mobileNumber,emailId):
            while(True):
                print("1.dosa")
                print("2.idly")
                print("3.meat")
                print("4.Paneer")
                print("5.Roti")
                option=int(input("enter your option:"))
                if option==1:
                    dish1=int(input("how many dosa u want:"))
                    menudict["dosa"]=menudict["dosa"]+dish1
                if option==2:
                    dish2=int(input("how many idly u want:"))
                    menudict["idly"]=menudict["idly"]+dish2
                if option==3:
                    dish3=int(input("how many meat u want:"))
                    menudict["meat"]=menudict["meat"]+dish3
                if option==4:
                    dish4=int(input("how many Paneer u want:"))
                    menudict["Paneer"]=menudict["Paneer"]+dish4
                if option==5:
                    dish5=int(input("how many Roti u want:"))
                    menudict["Roti"]=menudict["Roti"]+dish5  
                if option ==6:
                    break          
                #if validate(name,mobileNumber,emailId):
            k.addCustomer(name, mobileNumber, emailId,menudict)
            result = Collection_name.insert_many(clist)
            print(result.inserted_ids)
        else:

            print("Please enter correct infomation ")
            continue
                
    if choice==2:
        result = Collection_name.find()
        li=[]
        for i in result:
            li.append(i)
        print(li)
        #result.clear()
               
    if choice==3:
        p = input("enter the customer name")
        result1 = Collection_name.find({"name":p})
        li = []
        for i in result1:
            li.append(i)
        print(li)

    if choice==4:
        q= input('enter the customer name')
        result=Collection_name.delete_one({'name':q})
        print(result.deleted_count)

    if choice==5:
        name=input("enter the customer information u want to update")
        emailId=input("enter the customer email u want to update")
        result=Collection_name.update_one({"name":name},{"$set":{"emailId":emailId}})
        print("data has been modified")
        #print(result.modified_count)
    if choice==6:
        result=Collection_name.find({"name":name})
        result1=Collection_name1.find_one()
        for i in result:
            a=i['menudict']
            message1 = "Dosa " +str( a['dosa']*result1['dish1'])+ "\nidly" +str(a["idly"]*result1["dish2"])+ "\n meat" +str(a["meat"]*result1["dish3"])+  "\n Paneer" +str(a["Paneer"]*result1["dish4"]) + "\n Roti" +str(a["Roti"]*result1["dish5"])
            message1=message1+"\n Your bill "+str ((a['dosa']*result1['dish1'])+(a["idly"]*result1["dish2"])+(a["meat"]*result1["dish3"])+(a["Paneer"]*result1["dish4"])+(a["Roti"]*result1["dish5"]))
            message="Your total amount is " +str(message1)
            print(message)
            connection=smtplib.SMTP("smtp.gmail.com",587)
            connection.starttls()
            connection.login("Arifkhanstar0786@gmail.com","Absrkhan078621")
            connection.sendmail("Arifkhanstar0786@gmail.com",i["emailId"],message)
            connection.quit
            print("Mail sent successfully")
    if choice==7:
        break



# import json,smtplib,re,logging,time
# clist=[]
# class Customer:
#     def addCustomer(self,name,mobileNumber,emailId,dish1,dish2,dish3,dish4,dish5):
#         current_time=time.strftime("%m-%d-%Y %H:%M:%S",time.localtime())
#         dict1={"name":name,"mobileNumber":mobileNumber,"emailId":emailId,"dish1":dish1,"dish2":dish2,"dish3":dish3,"dish4":dish4,"dish5":dish5,"AddOn":current_time}
#         clist.append(dict1)
# k=Customer()
# def validate(name,mobileNumber,emailId):
#         name1=re.search("[A-Za-z]{0,25}$",name)
#         #print(name1)
#         mobileNumber1=re.search("(+91)[0]?(91)?[6-9]\d{9}$",mobileNumber)
#         #print(mobileNumber1)
#         emailId1=re.search( r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',emailId)
#         #print(emailId1)   
#         if name1 and  mobileNumber1 and emailId1:
#             return True
#         else:
#             return False   
# while(True):
#     print("1.Add Customer")
#     print("2. view Customer")
#     print("3.View all Customer details using JSON File")
#     print("4.Send an email to all customer")
#     print("5.Search customer based on name")
#     print("6.Exit")
#     choice=int(input("Enter your choice :"))
#     if choice==1:
#         name = input("Enter the name of Customer")
#         mobileNumber=input("Enter the mobilenumber:")
#         emailId=input("Enter the email:")
#         dish1=input("Enter the dish1:")
#         dish2=input("Enter the dish2 :")
#         dish3=input("Enter the dish3 :")
#         dish4=input("Enter the dish4 :")
#         dish5=input("Enter the dish5 :")
#         num1 = int(input("Enter the number of dish1:"))
#         num2 = int(input("Enter the number of dish2: "))
#         num3 = int(input("Enter the number of dish3: "))
#         num4= int(input("enter the number of dish4:"))
#         num5=int(input("enter the number of dish5:"))
#         if validate(name,mobileNumber,emailId):
#             k.addCustomer(name, mobileNumber, emailId, dish1, dish2, dish3, dish4, dish5)
#         else:
#             print("Please enter correct infomation ")
#             continue
#         break
#     if choice==2:
#             print(clist)
#     if choice==3:
#         jsondata=json.dumps(clist)
#         with open("mcustomer.json","w+",encoding="utf-8") as c1:
#             c1.write(jsondata)

#     if choice==4:
#         cprod=input("Enter customer want  to search: ")
#         print(list(filter(lambda i:i["name"]==cprod,clist)))
#         jsondata=json.dumps(clist)
#         with open("ncustomer.json","w+",encoding="utf-8") as s2:
#             s2.write(jsondata)

#     if choice==5:
#         for i in clist:
#             message =i["dish1"]*20+i["dish2"]*10+i["dish3"]*50+i["dish4"]*60+i["dish5"]*70
#             message=str(i)
#             print(message)
#             connection=smtplib.SMTP("smtp.gmail.com",587)
#             connection.starttls()
#             connection.login("Arifkhanstar0786@gmail.com","Absrkhan078621")
#             connection.sendmail("Arifkhanstar0786@gmail.com",i["emailId"],message)
#             connection.quit
#             print("Mail sent successfully")

#     if choice==6:
#         break





# # import json,smtplib,re,logging
# # clist=[]
# # class Customer:
#     def addCustomer(self,name,mobileNumber,emailId,dish1,dish2,dish3,dish4,dish5):
#         self.name=name
#         self.mobileNumber=mobileNumber
#         self.emailId=emailId
#         self.dish1=dish1
#         self.dish2=dish2
#         self.dish3=dish3
#         self.dish4=dish4
#         self.dish5=dish5
#         cust1=[self.name,self.mobileNumber,self.emailId,self.dish1,self.dish2,self.dish3,self.dish4,self.dish5]
#         return cust1
    
# k=Customer()
# def validate(name,mobileNumber,emailId):
#         name1=re.search("[A-Za-z]{0,25}$",name)
#         print(name1)
#         mobileNumber1=re.search("(+91)[0]?(91)?[6-9]\d{9}$",mobileNumber)
#         print(mobileNumber1)
#         emailId1=re.search( r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',emailId)
#         print(emailId1)   
#         if name1 and  mobileNumber1 and emailId1:
#             return True
#         else:
#             return False
# try:
#    if _name_ == "_main_":
#        while(True):
#         print("1.Add Customer")
#         print("2. view Customer")
#         print("3.View all Customer details using JSON File")
#         print("4.Send an email to all customer")
#         print("5.Search customer based on name")
#         print("6.Exit")
#         choice=int(input("Enter your choice :"))
#         if choice==1:
#             name = input("Enter the name of Customer")
#             mobileNumber=input("Enter the mobilenumber:")
#             emailId=input("Enter the email:")
#             dish1=input("Enter the dish1:")
#             dish2=input("Enter the dish2 :")
#             dish3=input("Enter the dish3 :")
#             dish4=input("Enter the dish4 :")
#             dish5=input("Enter the dish5 :")
#             num1 = int(input("Enter the number of dish1:"))
#             num2 = int(input("Enter the number of dish2: "))
#             num3 = int(input("Enter the number of dish3: "))
#             num4= int(input("enter the number of dish4:"))
#             num5=int(input("enter the number of dish5:"))
#             if validate(name,mobileNumber,emailId):
        
#                 u=k.addCustomer(name,mobileNumber,emailId,dish1,dish2,dish3,dish4,dish5)
#                 totalbill=dish1+dish2+dish3+dish4+dish5
#                 di1={"totalbill":totalbill}
#                 print(di1)
                    
#                 customer1=["name","mobileNumber","emailId","dish1","dish2","dish3","dish4","dish5"]
                    
#                 for i in range(len(u)):
#                     di1[customer1[i]]=u[i]
                    
#                     clist.append(di1)
#                     print(clist)
#             else:
#                 logging.error("wrong")
            
            
#         if choice==2:
#                 print(clist)
#         if choice==3:
#             jsondata=json.dumps(clist)
#             with open("mcustomer.json","w+",encoding="utf-8") as c1:
#                 c1.write(jsondata)

#         if choice==4:
#             cprod=input("Enter customer want  to search: ")
#             print(list(filter(lambda i:i["name"]==cprod,clist)))
#             jsondata=json.dumps(clist)
#             with open("ncustomer.json","w+",encoding="utf-8") as s2:
#                 s2.write(jsondata)

#         if choice==5:
#             for i in clist:
#                 message =i["dish1"]*20+i["dish2"]*10+i["dish3"]*50+i["dish4"]*60+i["dish5"]*70
#                 message=str(i)
#                 print(message)
#                 connection=smtplib.SMTP("smtp.gmail.com",587)
#                 connection.starttls()
#                 connection.login("Arifkhanstar0786@gmail.com","Absrkhan078621")
#                 connection.sendmail("Arifkhanstar0786@gmail.com",i["emailId"],message)
#                 connection.quit
#                 print("Mail sent successfully")

#         if choice==6:
#             break
# except:
#     logging.error("something went wrong")





# import re,logging,csv,datetime,time
# header = ["title","author","description","price","distributor","publisher","AddOn"]
# booklis=[]
# class BookDetails:
#     def AddBook(self,title,author,description,price,distributor,publisher):
#         current_time=time.strftime("%m-%d-%Y %H:%M:%S",time.localtime())
#         dict1={"title":title,"author":author,"description":description,"price":price,"distributor":distributor,"publisher":publisher,'AddOn':current_time}
#         booklis.append(dict1)
# k=BookDetails()

# def valid_book(bookn,price):
#     val=re.match("([a-z]+)([a-z]+)([a-z]+)$",bookn)
#     val2=re.match("[0-9]{0,7}$",price)
#     if val and val2:
#         return True
#     else:
#         return False

# try:
#     if _name=="main_":
#         while(True):
#           print("1. add book ")
#           print("2. view book ")
#           print("3. sorted order of book on basis of title ")
#           print("4. search book using title")
#           print("5.view in csv")
#           print("6. exit")
#           choice=int(input("Enter a choice: "))
#           if choice==1:
#              while(True):
#                 title=input("Enter title of book: ")
#                 price=input("Enter price of book: ")
#                 if valid_book(title,price):
#                    author=input("Enter author of book: ")
#                    description=input("Enter description of book: ")
#                    distributor=input("Enter distributor of book: ")
#                    publisher=input("Enter publisher of book: ")
#                    k.AddBook(title,price,author,description,distributor,publisher)
#                 else:
#                     print("Please enter correct infomation ")
#                     continue
#                 break
                    
#           if choice==2:
#               print(booklis)
#           if choice==3:
#             print(sorted(booklis,key=lambda i:i["title"]))
#           if choice==4:
#             search1=input("Enter title to search product: ")
#             print(list(filter(lambda x:x["title"]==search1,booklis)))
#           if choice==5:
#             with open('Bookk.csv','w+',encoding='UTF8',newline='') as b:
#                 writer = csv.DictWriter(b,fieldnames=header)
#                 writer.writeheader()
#                 writer.writerows(booklis)
#           if choice==6:
#                break
# except:
#     logging.error("Something went wrong")

# import re
# import logging
# import time
# import csv
# try:
# headerContent=["ProductName","description","price","manufacturing","expiry","addedon"]
# prodlist=[]  
# class productdetails():
#     def addProductdetails(self,Product_Name,description,temp_price,manufacturing,expiry):
#         current_local_time=time.strftime("%Y-%m-%d ",time.localtime())
#         dict1={"Product_Name":Product_Name,"description":description,"temp_price":temp_price,"manufacturing":manufacturing,"expiry":expiry,"addedon":current_local_time}
#         prodlist.append(dict1)
# obj1=productdetails()
# def valid_product(ProductName,price):
#     val1=re.match("([A-Z]+)([a-z]+)([a-z]+)$",ProductName)
#     val2=re.match("[0-9]{0,7}$",price)
#     if val1 and val2:
#         return True
#     else:
#         return False
# while(True):
#     print("1. Add Product:")
#     print("2. display product details: ")
#     print("3. search product using product Name")
#     print("4. list product that expire today")
#     print("5. exit")
    
#     try:
#      choice=int(input("enter your choice: "))
#      except Exception:
#          logging.error("something went wrong")
#          continue
    
#      if choice==1:
#         while(True):
#             Product_Name=input("Enter product Name: ")
#             temp_price=input("enter the price: ")
#             if valid_product(Product_Name, temp_price):
#                 description=input("enter the description:")
#                 manufacturing=input("enter date manufacturing date in mm-dd-yyyy format" )
#                 expiry=input("enter date expiry date  mm-dd-yyyy format" )   
#                 obj1.addProductdetails(Product_Name,description,temp_price,manufacturing,expiry)  
#             else:
#                 print("Please  entered valid product name and price")
#                 continue
#             break 
#      if choice==2:
#         print(prodlist)
#      if choice==3:
#         sprod=input("Enter product want  to search: ")
#         print(list(filter(lambda i:i["Product_Name"]==sprod,prodlist)))
#      if choice==4:
#         local_current_time=time.localtime()
#         find_date=time.strftime("%m-%d-%Y",local_current_time)
#         expire=(list(filter(lambda i:i["expiry"]==find_date,prodlist)))
#         print(expire)
            
            
#             #current_local_time=time.strftime("%m-%d-%Y ",time.localtime())
#             #if (current_local_time==expiry ):
#             #    print (ProductName)
#             ## print ('Renew License Soon')
#      if choice==5:
#          with open("file2.csv","w+",encoding="UTF8",newline="") as s:
#             writer=csv.DictWriter(s,fieldnames=headerContent)
#             writer.writeheader()
#             writer.writerows(prodlist)

#      if choice==6: 
#          break
# except Exception:
#     logging.error('something went wrong')
# finally:
#     print("thank you")






# # from datetime import datetime
# # import time
# # import re
# # import csv
# # header=['productname','description','price','manufracturingdate','expirydate']
# # productlist=[]
# # class ProductDetails:
# #     def addproductdetails(self,productname,description,price,manufracturingdate,expirydate):
        
# #         dict1={"productname":productname,"description":description,"price":price,"manufracturingdate":manufracturingdate,"expirydate":expirydate,}
# #         productlist.append(dict1)
# # obj1=ProductDetails()
# # def validate(productname,price):
# #     valproductname=re.search("[A-Z]{1}[^A-Z]{0,25}$",productname)
# #     valprice=re.search("[0-9]{0,7}$",price)
# #     if valproductname and valprice:
# #         return True
# #     else:
# #         return False
# # while(True):
# #     print("1.Add products:")
# #     print("2.view all products:")
# #     print("3.Search a product:")
# #     print("4.list all products expire today:")
# #     print("5.header")
# #     print("6.exit")
# #     choice=int(input("enter your choice"))
# #     if choice==1:
# #         while(True):
# #             product_name=input("enter the product name:")
# #             price_=input("enter price :")
# #             if validate(product_name,price_):
# #                 description=input("enter description:")
# #                 manufracturingdate=str(input("Enter mfdate(yyyy-mm-dd):"))
# #                 print(datetime.strptime(manufracturingdate, "%Y-%m-%d"))
# #                 expirydate=str(input("enter epdate(mm-dd-yyyy):"))
# #                 print(datetime.strptime(expirydate, "%m-%d-%Y"))
# #                 obj1.addproductdetails(product_name,description,price_,manufracturingdate,expirydate)
# #             else:
# #                 print("Please  entered valid product name and price")
# #                 continue
# #             break
# #     if choice==2:
# #         print(productlist)
# #     if choice==3:
# #         sproduct=input("enter your product to search:")
# #         print(list(filter(lambda i:i["productname"]==sproduct,productlist)))
# #     if choice==4:
# #         local_current_time=time.localtime()
# #         find_date=time.strftime("%m-%d-%Y",local_current_time)
# #         expire=(list(filter(lambda i:i["expirydate"]==find_date,productlist)))
# #         print(expire)
# #     if choice==5:
# #         with open('student1.csv','w+',encoding="UTF8",newline='') as s:
# #            writer=csv.DictWriter(s,fieldnames=header)
# #            writer.writeheader()
# #            writer.writerows(productlist)
# #     if choice==6:
# #         break



# # import re
# # import time
# # import csv
# # headerContent=["ProductName","description","price","manufacturing","expiry","addedon"]
# # prodlist=[]  
# # class productdetails():
# #     def addProductdetails(self,Product_Name,description,temp_price,manufacturing,expiry):
# #             current_local_time=time.strftime("%Y-%m-%d ",time.localtime())
# #             dict1={"Product_Name":Product_Name,"description":description,"temp_price":temp_price,"manufacturing":manufacturing,"expiry":expiry,"addedon":current_local_time}
# #             prodlist.append(dict1)
# # obj1=productdetails()
# # def valid_product(ProductName,price):
# #     val1=re.match("([A-Z]+)([a-z]+)([a-z]+)$",ProductName)
# #     val2=re.match("[0-9]{0,7}$",price)
# #     if val1 and val2:
# #         return True
# #     else:
# #         return False
# # while(True):
# #     print("1. Add Product:")
# #     print("2. display product details: ")
# #     print("3. search product using product Name")
# #     print("4. list product that expire today")
# #     print("5. exit")
    

# #     choice=int(input("enter your choice: "))
    
        
# #     if choice==1:
# #         while(True):
# #             Product_Name=input("Enter product Name: ")
# #             temp_price=input("enter the price: ")
# #             if valid_product(Product_Name, temp_price):
# #                 description=input("enter the description:")
# #                 manufacturing=input("enter date manufacturing date in mm-dd-yyyy format" )
# #                 expiry=input("enter date expiry date  mm-dd-yyyy format" )   
# #                 obj1.addProductdetails(Product_Name,description,temp_price,manufacturing,expiry)  
# #             else:
# #                 print("Please  entered valid product name and price")
# #                 continue
# #             break 
# #     if choice==2:
# #         print(prodlist)
# #     if choice==3:
# #         sprod=input("Enter product want  to search: ")
# #         print(list(filter(lambda i:i["Product_Name"]==sprod,prodlist)))
# #     if choice==4:
# #         local_current_time=time.localtime()
# #         find_date=time.strftime("%m-%d-%Y",local_current_time)
# #         expire=(list(filter(lambda i:i["expiry"]==find_date,prodlist)))
# #         print(expire)
            
            
# #             #current_local_time=time.strftime("%m-%d-%Y ",time.localtime())
# #             #if (current_local_time==expiry ):
# #             #    print (ProductName)
# #             ## print ('Renew License Soon')
# #     if choice==5:
# #         with open("file2.csv","w+",encoding="UTF8",newline="") as s:
# #             writer=csv.DictWriter(s,fieldnames=headerContent)
# #             writer.writeheader()
# #             writer.writerows(prodlist)

# #     if choice==6:    
# #         break