import math 
result=1
for i in range(1,21):
    result=int((result*i)/math.gcd(result,i))
print(result)
