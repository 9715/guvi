d=int(input())
c=0
while(d%2==0):
    print(int(d/2))
    d=int(d/2)
    c=1
if c == 0:
    print(d)
