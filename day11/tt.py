# import time
# current_time=time.localtime()
# #print(current_time)
# current_clock_time=time.strftime("%y/%m/%d-%H:%M:%S")
# print(current_clock_time)


li =[{'name': 'gullu', 'rollno': 1, 'admino': 123, 'Maths': 89, 'Science': 89, 'Hindi': 7, 'English': 7, 'Social': 6, 'total': 198, 'AddOn': '21-08-03  08:29:28'}, 
{'name': 'ritik', 'rollno': 2, 'admino': 234, 'Maths': 87, 'Science': 98, 'Hindi': 7, 'English': 8, 'Social': 7, 'total': 207, 'AddOn': '21-08-03  08:29:42'}, 
{'name': 'ram', 'rollno': 3, 'admino': 4, 'Maths': 56, 'Science': 7, 'Hindi': 8, 'English': 5, 'Social': 6, 'total': 82, 'AddOn': '21-08-03  08:29:55'}]
marks=[]
for i in li:
    marks.append(i['total'])
print(sorted(marks))

# n = int(input())
# # lii=[]
# # for i in li:
# #     if(i['salary']>=n):
# #         lii.append(i)
# # print(lii)
# new_li = [i for i in li if i['salary']>=n]
# print(new_li)
# n = int(input('enter the salary'))
# def sal(li,n):   
#     new_li=[x for x in li if x['salary']>=n]
#     return new_li 
# print(sal(li,n)) 

# import collections
# import re,time
 
# def timeDate():
#     time1 = time.localtime()
#     current_colck_time = time.strftime("%Y-%m-%d %H:%M:%S",time1)
#     return current_colck_time
 
# while (True):
#      print("enter your choice:")
#      print("1.ADD_EMPLOYEE")
#      print("2.VIEW_EMPLOYEE")
#      print("3.EXIT")
 
#      choice = int(input("enter your choice: "))
 
#      if choice == 1 :
#          print("You selected ADD_EMPLOYEE ")
#          Emp_ID = input("enter emp id : ")
#          val = re.search("^E\d{4}$",Emp_ID)
#          Emp_name = input("enter emp name: ")
         
#          Emp_Desgination = input("enter a desgination: ")
#          val1 = re.search("^[a-zA-Z]$",Emp_Desgination)
         
#          Emp_salary = input("enter salary : ")
#          val2 = re.search("^[1-9]\d{6}$",Emp_salary)
         
#          Emp_address = input("enter a address:")
         
#          Emp_phone_No = input("enter a Phone_Number: ")
#          val3 = re.match("^\+91?[6-9]\d{9}$",Emp_phone_No)
       
#          Emp_pincode = input("enter a pincode: ")
#          val4 = re.search("^6\d{5}$",Emp_pincode)
 
#          T_D = timeDate()
         
 
         
#      if choice == 2:
#          print("You selected to view employee Details")
#          dict1 = { "Emp_Id":Emp_ID,"Emp_name": Emp_name,"Emp_desgination":Emp_Desgination,
#                    "Emp_salary":Emp_salary,"Emp_address":Emp_address,"Emp_phone no": Emp_phone_No,
#                    "Emp_pincode":Emp_pincode,"timededOn":T_D}
#          #dict2 = { "Emp_address":Emp_address,"Emp_phone no": Emp_phone_No,"Emp_pincode":Emp_pincode}
#          emp_dict = collections.ChainMap(dict1)
#          print(emp_dict.maps)
 
                 
         
#      if choice == 3:
#          print("EXIT")
#          break
#      else:
#         print("Thank you")
 