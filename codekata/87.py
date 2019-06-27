k,l=list(map(int,input().split()))
s=[]
for i in range(1,100):
    if k%i==0 and l%i==0:
        s.append(i)
print(max(s))
