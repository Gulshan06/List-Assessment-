import re,logging,csv,datetime,time
header = ["title","author","description","price","distributor","publisher","AddOn"]
booklis=[]
class BookDetails:
    def AddBook(self,title,author,description,price,distributor,publisher):
        current_time=time.strftime("%m-%d-%Y %H:%M:%S",time.localtime())
        dict1={"title":title,"author":author,"description":description,"price":price,"distributor":distributor,"publisher":publisher,'AddOn':current_time}
        booklis.append(dict1)
k=BookDetails()

def valid_book(bookn,price):
    val=re.match("([a-z]+)([a-z]+)([a-z]+)$",bookn)
    val2=re.match("[0-9]{0,7}$",price)
    if val and val2:
        return True
    else:
        return False

try:
    if _name=="main_":
        while(True):
          print("1. add book ")
          print("2. view book ")
          print("3. sorted order of book on basis of title ")
          print("4. search book using title")
          print("5.view in csv")
          print("6. exit")
          choice=int(input("Enter a choice: "))
          if choice==1:
             while(True):
                title=input("Enter title of book: ")
                price=input("Enter price of book: ")
                if valid_book(title,price):
                   author=input("Enter author of book: ")
                   description=input("Enter description of book: ")
                   distributor=input("Enter distributor of book: ")
                   publisher=input("Enter publisher of book: ")
                   k.AddBook(title,price,author,description,distributor,publisher)
                else:
                    print("Please enter correct infomation ")
                    continue
                break
                    
          if choice==2:
              print(booklis)
          if choice==3:
            print(sorted(booklis,key=lambda i:i["title"]))
          if choice==4:
            search1=input("Enter title to search product: ")
            print(list(filter(lambda x:x["title"]==search1,booklis)))
          if choice==5:
            with open('Bookk.csv','w+',encoding='UTF8',newline='') as b:
                writer = csv.DictWriter(b,fieldnames=header)
                writer.writeheader()
                writer.writerows(booklis)
          if choice==6:
               break
except:
    logging.error("Something went wrong")

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