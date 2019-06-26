g=list(input())
if len(g)%2==0:
    g[int(len(g)/2)] ='*'
    g[int(len(g)/2)-1]='*'
else:
    g[int(len(g)/2)] ='*'
for i in range(0,len(g)):
    print(g[i],end='')
