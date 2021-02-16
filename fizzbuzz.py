def fizbuz(n):
    for i in range(1,n):
        if(i%15==0):
            print("fizzbuzz")
            continue
        elif(i%3==0):
            print("fizz")
            continue
        elif(i%5==0):
            print("buzz")
            continue
        print(i)
fizbuz(21)
            
