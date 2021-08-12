# # l=[{'name': 'gullu', 'rollno': '12', 'admno': '12345', 'college': 'rjit', 'parentname': 'bl', 'mobilenumber': '9131', 'emailid': 'gullu@gmail.com', 'sub1mark': 34, 'sub2mark': 56, 'sub3mark': 65, 'sub4mark': 54, 'sub5mark': 45}]
# import operator
# l=[{'name': 'gullu', 'rollno': '12', 'admno': '123', 'college': 
# 'rjit', 'parentname': 'bl', 'mobilenumber': '9131', 'emailid': 'gulu', 'sub1mark': 22, 'sub2mark': 33, 'sub3mark': 44, 'sub4mark': 55, 'sub5mark': 66, 'total': 220},
# {'name': 'gullu', 'rollno': '12', 'admno': '123', 'college': 
# 'rjit', 'parentname': 'bl', 'mobilenumber': '9131', 'emailid': 'gulu', 'sub1mark': 22, 'sub2mark': 33, 'sub3mark': 44, 'sub4mark': 55, 'sub5mark': 66, 'total': 200},
# {'name': 'gullu', 'rollno': '12', 'admno': '123', 'college': 
# 'rjit', 'parentname': 'bl', 'mobilenumber': '9131', 'emailid': 'gulu', 'sub1mark': 22, 'sub2mark': 33, 'sub3mark': 44, 'sub4mark': 55, 'sub5mark': 66, 'total': 210}]
# new_li=[x for x in l if x["total"]<250]
# # listToStr = ' '.join([str(elem) for elem in new_li])
# li=[x['emailid'] for x in new_li ]
# print(li)


# l.sort(key=operator.itemgetter('total'))
# print(l[::-1])
# import re
# m = input()
# # # val = re.search('^(\d{1,2}|100)$',m)
# val = re.search("^(40|[1-3][0-9]?)$",m)
# # v6=re.match("^(40|[1-3][0-9]?)$",sub1)
# if val:
#     print("true")
# else:
#     print('no')
final_total = 600
discount = 0
if (final_total > 500 and final_total <=1000):
    f = (final_total/100)*10
    discount = final_total - f
print(discount)
