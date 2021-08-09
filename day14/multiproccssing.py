import time, multiproccssing
def square(li):
    for i in li:
        print(i*i)

def cube(li):
    for i in li:
        print(i*i*i)
 
li = [2,3,4,5,6]
t1 = multiproccssing.Process(target=square,args=(li,))
t2 = multiproccssing.Process(target=cube,args=(li,))
t1.start()
t2.start()
t1.join()
t2.join()
print("...")

