a=list(map(str,input().split()))
Count=0
for i in range(len(a)):
  Count=Count+len(a[i])
print(Count)
