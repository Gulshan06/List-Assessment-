import threading,time

def number():
    for i in range(1,10):
        time.sleep(3)
        print(i)
# number()
def hello():
    for i in range(1,5):
        time.sleep(3)
        print('hello')


t1=threading.Thread(target=number)   #  way to create the thread 
t2 = threading.Thread(target=hello)
t2.start()
t1.start()    # for excute 
t1.join()
t2.join()
print("......")