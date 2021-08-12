import collections
import re, time,csv
try:
    header =["name","id","designation","salary","address","phone","pincode","AddOn"]
    print("Select an option from menu")
    print("\n")
    print("1. AddEmp")
    print("2. ViewEmp")
    print("3. Check the employee with salary")
    print("4. Generate CSV file")
    choice=int(input("enter the choice"))
    def addtimedate():
        time1=time.localtime()
        currenttime= time.strftime("%y-%m-%d  %H:%M:%S")
        return currenttime
    li=[]
    if(choice==1):
        a = int(input('Enter the no how many details you want to fill'))
        for i in range(a):
            dict={}
            print("AddEmp is Details")
            dict["name"]=input("enter the empname:")
            dict["id"]=input("enter the emp id:")
            dict["designation"]=input("enter the designation:")
            salary=input("enter the salary:")
            amount=re.search("^[0-9]",salary)
            if amount:
                dict['salary']=int(salary)
            dict["address"]=input("enter the address:")
            # dict["phone"]=input("enter the phone no:")
            phn =input("enter the phone no:")
            validation=re.search("^[6-9]\d{9}$",phn)
            if validation:
                dict["phone"]=phn
            pincode=input("enter the pincode:")
            validation1=re.search("^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$",pincode)
            if validation1:
                dict['pincode']=pincode
            dict['AddOn']=addtimedate()
            li.append(dict)
    if(choice==2):
        print(li)
    if choice==3:
        n = int(input('enter the salary'))
        def sal(li,n):   
            new_li=[x for x in li if x['salary']>=n]
            return new_li 
        print(sal(li,n))
    if choice==4:
        with open('Employee.csv','w+',encoding='UTF8',newline='') as s:
            writer = csv.DictWriter(s,fieldnames=header)
            writer.writeheader()
            writer.writerows(li)

        # n = int(input('enter the salary'))
        # check= [x for x in li if x["salary"]>=n]
        # print(check)
except Exception:
    print("something went wrong")
else:
    print('your program is completed successfully')
finally:
    print("Thank you!!")