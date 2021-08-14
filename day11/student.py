import sys,re,time,csv
try:
    header =['total','name','rollno','class','english','hindi','maths','science','social','AddOn']
    student= []
    class StudentData:
        def addDetails(self,name,rollno,class,english,hindi,maths,science,social):
            totalmarks=english+hindi+maths+science+social
            current_time=time.strftime("%Y-%M-%d %H:%M:%S",time.localtime())
            dict1 = {'total':totalmarks,'name':name,'rollno':rollno,'class':class,'english':english,'hindi':hindi,'maths':maths,'science':science,'social':social,'AddOn':current_time}
            student.append(dict1)
    # def val(rollno,admin,english,hindi,maths,science,social):
    #             val=re.search("^[1-9]",rollno)
    #             val1=re.search('^[1-9]',admin)
    #             val2=re.search('^[0-9]',english)
    #             val3=re.search('^[0-9]',maths)
    #             val4=re.search('^[0-9]',social)
    #             val5=re.search('^[0-9]',hindi)
    #             val6=re.search('^[0-9]',science)
    #             if val and val1 and val2 and val3 and val4 and val5 and val6:
    #                 return [int(rollno),int(admin),int(english),int(maths),int(social),int(hindi),int(science)]
    #             else:
    #                 print("you had enter wrong input")
    #                 sys.exit()
    obj1=StudentData()
    while(True):
        print("1. Add student details - ")
        print("2. Display student details Like API - ")
        print("3. Search student by Rollno - ")
        print("4. Ranking - ")
        print("5. Exit - ")
        print('6. save to file - ')
        choice = int(input('enter your choice - '))
        if choice==1:
            name = input("enter the name of student - ")
            rollno=input("enter the Rollno - ")
            admin=input('enter the admin no -  ')
            english=input("enter the english marks: ")
            maths=input("enter the maths marks: ")
            social=input("enter the social marks: ")
            hindi=input("enter the hindi marks: ")
            science=input("enter the science marks: ")
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
        if choice == 6:
            with open('student.csv','w+',encoding='UTF8',newline='') as s:
                writer = csv.DictWriter(s,fieldnames=header)
                writer.writeheader()
                writer.writerows(student)
except Exception:
    print("something went wrong")
finally:
    print("Thank you!!")

