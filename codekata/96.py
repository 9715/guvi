A,B,H=map(int,input().split())
sum = 0
for i in range(1,H+1):
	sum=sum+A+(i-1)*B
print(sum)
