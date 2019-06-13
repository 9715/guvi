a,b=map(int,input().split())
for i in range(a,b+1):
  temp=i
  sum=0
  while(i>0):
   r=i%10
   sum=sum+(r*r*r)
   i=i//10
  if(temp==sum):
   print(sum)
