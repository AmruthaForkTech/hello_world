import math
def primefac(n):
    while n%2==0:
        print("2")
        n=n//2
        
    for i in range(3,n,2):
        while n%i==0:
            print(i)
            n=n//i
            
primefac(36)
