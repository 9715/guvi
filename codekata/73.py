n=int(input())
g,k=map(int,input().split())
for i in range(g,k+1):
  if(n==i):
   print("yes")
   break
else:
   print("no")
