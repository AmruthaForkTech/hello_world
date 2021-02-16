def palindrome(str1):
    for i in range(0,len(str1)):
        if str1[i]==str1[len(str1)-i-1]:
            return True
        return False

result=palindrome("saas")
if(result):
   print("yes,the string is palindrome")
else:
    print("no,the string is not a palindrome")
    







    
        
