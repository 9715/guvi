num = int(input("enter the number"))
sum = 0
 
for n in range(num):
    numbers = float(input())
    sum += numbers
 
avg = sum/num
print('Average of ', num, ' numbers is :', avg)
