"""
Write a Python program to input marks for five
subjects Physics, Chemistry, Biology, Mathematics,
and Computer. Calculate the percentage and grade
according to the following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Grade F
"""
phy = int(input("Enetr physics marks : "))
chem = int(input("Enetr chemistry marks : "))
bio = int(input("Enetr biology marks : "))
math = int(input("Enetr mathematics marks : "))
comp = int(input("Enetr computer marks : "))
total = phy + chem + bio + math + comp
per = total / 5
if per >= 90:
    print("Your Grade Is A")
elif per >= 80:
    print("Your Grade Is B")
elif per >= 70:
    print("Your Grade Is C")
elif per >= 60:
    print("Your Grade Is D")
elif per >= 40:
    print("Your Grade Is E")
else:
    print("Your Grade Is F")