d={'a':1,'b':2,'d':2,'c':3}
# a=[]
# b={}
# for key,val in d.items():
#     if val not in a:
#         a.append(val)
#         b[key]=val
# print(str(b))
# d=frozenset(d)
# print(d)
d={}
print(d)
k=list(input("keys: ").split(","))
v=list(map(int,input("values: ").split(",")))
d=dict(zip(k,v))
print(d)
a=list(input().split(","))
d[a[0]]=int(a[1])
print(d)