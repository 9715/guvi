s2=list(input())
p=[]
for i in s2:
    if i not in p:
        p.append(i)
if s2==p:
    print("Yes")
else:
    print("No")
