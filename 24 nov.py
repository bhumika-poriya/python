x = int(input())
y = int(input())
z = int(input())
n = int(input())
a= [[b,c,d] for b in range(x+1) for c in range(y+1) for d in range(z+1) if(b+c+d!=n)]
print(a)