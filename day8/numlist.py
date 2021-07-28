# li = [1,2,3,4,5,6,7,8,9,10]
# new = [i for i in li if i%2==0 ]
# print(new)

li=['english','tamil','civic','river','rotor','madam','malayalam','example','running','noon']
# new = [i for i in li if i==i[::-1]]
# print(new)

# li =[i for i in range(2,500)]
# new=[j for j in li if j%2==1]
# print(new)
# new = [i.upper() for i in li ]
# print(new)

new = [i.replace('noon','mooring') for i in li ]
print(new)
