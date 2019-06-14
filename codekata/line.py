b=str(input())
count=1
special="."
for i in range(len(b)):
   if(b[i] in special):
     count=count+1
print(count)
