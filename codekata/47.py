a=int(input())
n=[int(i) for i in input().split()]
n.sort()
print(n[0],end=" ")
print(n[a-1])
