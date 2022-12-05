def length(str1):
    print(len(str1))
    x=['a','e','i','o','u','A','E','I','O','U']
    r=''
    for i in range(len(str1)):
        if str1[i] not in x:
            r=r+str1[i]
    print(len(r))
x=input()
length(x)