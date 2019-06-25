a=int(input())
b=0
c=0
for i in range (0,a):
    b=2**i
    if b == a:
        print("yes")
        c=1
        break
if c == 0:
    print("no")
