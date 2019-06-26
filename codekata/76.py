p=int(input())
s=int(p/2)
q=0
for i in range (2,s+1):
    if p % i == 0:
        q=1
        print("yes")
        break
if q == 0:
    print("no")
