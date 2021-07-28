movie =['harry potter','spiderman','superman','master','life']

# # for i in movie:
#     if 'a' in i:
#         new.append(i)
new = [i for i in movie if 'a' in i]
print(new)