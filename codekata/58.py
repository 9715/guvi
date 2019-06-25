b,c=input().split()
b=int(b)
c=int(c)
arr=[int(x) for x in input().split()]
d=0
for i in arr:
    if i == c:
        print("yes")
        d=1
        break
if d == 0:
    print("no")
