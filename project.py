x=eval(input())
y=eval(input())
for x in range(x,y+1):
    a=eval(input(""))
    if a%2==0:
        print(a,"is an even number.")
    else:
        print(a,"is an odd number.")
    if a<0:
        print(a,"is a negative number.")
    else:
        print(a,"is a positive number.")
    if a>1:
        for i in range(2,a):
            if a%i==0:
                print(a,"is a composite number.")
                break
        else:
            print(a,"is a prime number.")
    else:
        print(a, "is neither prime nor composite number")
    
    