s=input()
k=[]
for i in s:
  if i.isnumeric():
    k.append(i)
print("".join(k))
