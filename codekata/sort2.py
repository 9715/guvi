b=int(input())
c=list(map(int,input().split()))
c.sort()
for i in range(len(c)):
  print(c[i],end=' ')
