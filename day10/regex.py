# "^hello"
# "hello$"
# "^hello$"


import re
# var ='90%'
# # regex=re.match('^(bc){2,4}$',var)
# # regex=re.match('(hello|hii)+x',var)
# # regex=re.match('[a-zA-Z0-9]{5}$',var)
# regex=re.match('^[a-zA-Z]{7}',var)
# regex=re.match('[0-9]{2}%$',var)
# print(regex)

num= input("Enter your phone no.: ")
val = re.search("^(\+91)?[0]?[91]?[6-9]\d{9}$",num)
if val:
    print('number accepted')
else:
    print("number rejected")