from typing import ChainMap


# ChainMap
import collections
dict1={'name':'rahul','age':22}
dict2={'name':'suraj','age':23}
dict ={'name':'ram','age':24}
comb_dic=collections.ChainMap(dict1,dict2)
print(comb_dic.maps)