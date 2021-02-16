def pangram_1(string):
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i not in string.lower():
            return False
        return True
result=pangram_1("the quick brown fox jumps over the dog")
if result==True:
    print("pangram")
else:
    print("not pangram")
