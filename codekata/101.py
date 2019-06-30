a,b=input().split()
a=list(a)
b=int(b)
m=len(a)
index=m-b
for i in range (index,m):
    print(a[i],end="")
