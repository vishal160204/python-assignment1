y=int(input("enter a number"))
if y % 5 == 0 and y % 3 ==0:
   print("BRUDITE-NIRVANA")
elif y % 3 == 0:
   print("SKILLBREW")
elif y % 5 == 0:
   print("BRUDITE")
else:
   print("number is not divisible by 3 or 5")