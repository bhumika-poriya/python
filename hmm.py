x=input()
print(x.upper())
for i in x:
    if i in ['a','e','i','o','u','A','E','I','O','U']:
        print(i,end=",")
print()
y=input()
if y in x:
    print(x.replace(y,''))


