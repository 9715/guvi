y=int(input())
if y%4==0 and y%100!=0:
  print("Leap year")
elif y%100==0:
  print("It is not a leap year")
elif y%400==0:
  print("It is a leap year")
else:
  print("It is not a leap year")
