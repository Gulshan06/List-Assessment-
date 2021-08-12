# # Nametuple()
# import collections
# employees= collections.namedtuple("employees",["name","empID","salary"])
# e1 = employees("Raju",100,2500)
# print(e1[1])

# orderedDict()
# import collections
# d1 = collections.OrderedDict()
# d1['name']='Ram'
# d1['rollno']='22'
# d1['admno']='213323'
# # print(d1)
# for key,Value in d1.items():
#     print(key,Value)

# counter()
# import collections
# from typing import Counter
# x = collections.Counter(['hello','Hello','hi'])
# print(x)
# import collections
# # li = list(map(str,input().split()))
# li = []
# x = int(input())
# for i in range(x):
#     a = input()
#     li.append(a)    
# x = collections.Counter(li)
# print(x)


# defaultDict()
import collections
x = collections.defaultdict(str)
# x = {'name':"rahul","rollno":"3"}
x['name']='rahul'
x['rollno']='12'
print(x)
print(x['admi'])
