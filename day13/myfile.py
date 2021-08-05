# myfile = open('file','w+b')

# myfile.write("hello ")
# a = input("enter the name")
# myfile.write(a+'\n')
# # myfile=open('file.txt','r+')
# myfile.seek(0)
# print(myfile.tell())  # check the position of curccer 
# x = myfile.read()
# print(x)
# # print(myfile.tell())
# myfile.close()


# ********** Binary file Operation **********


# myfile = open('file2','w+b')
# test=bytearray([12,12,12,1])
# myfile.write(test)
# myfile.close()

# ********Exception handling in file  *********** 

with open('file.txt','w+') as f:
    f.write("hello")
    f.seek(0)
    print(f.read())
    f.close()
