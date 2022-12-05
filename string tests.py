# s="pythonprogramming23"
# print(s.isalpha())
# print(s.isdigit())
# print(s.isupper())
# print(s.isalnum())
# print(s.rfind("p"))
# print(s.count("o"))
# print(s.endswith("w"))
# print(s.startswith("p"))
# print(s.find("java"))
# print(s.capitalize())
# print(s.upper())
# print(s.replace("pythonprogramming23","bhumika"))
def count(b,c):
    a=0
    for i in b:
        if i==c:
            a+=1
        else:
            continue
    return a
x=input()
y=input()
print(count(x,y))