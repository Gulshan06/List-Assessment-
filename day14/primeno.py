import threading,logging
try:
    low=2
    high=500
    def Prime():
        for num in range(low, high+1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    print(num)    
    def Palindrome():
        for num in range(10, 500 + 1):
            temp = num
            rev = 0
            while(temp > 0):
                Rem = temp % 10
                rev = (rev * 10) + Rem
                temp = temp //10
            if(num == rev):
                print(num)            
    if(__name__=="__main__"):
        p1=threading.Thread(target=Prime)
        p2=threading.Thread(target=Palindrome)
        p1.start()
        p1.join()
        p2.start()
        p2.join()
        print("*****")
except Exception:
    logging.error("something went wrong")
finally:
    print("Thank You!!")