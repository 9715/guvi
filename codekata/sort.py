n=int(input())
a=list(map(int,input().split()))
a.sort()
for i in range(len(a)):
  print(a[i],end=' ')
