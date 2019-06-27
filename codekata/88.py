n,m=map(int,input().split())
a=n
b=m
while(m):
  n,m=m,n%m
  c=(a*b)//n
print(c)
