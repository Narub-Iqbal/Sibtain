weight=float(input("Enter your weight in Kg: "))
h=float(input("Enter you Height in in Feet: "))
#converting height from foot to meters
height=h/3.2808
#square of height
height=height*height
bmi=weight/height
if bmi<18.5:
    print("Your bmi is: ",bmi," and you are Underweight")
elif bmi>=18.5 and bmi<=24.9:
    print("Good your bmi is: ",bmi," and your weight is normal")
elif bmi>=25 and bmi<=29.9:
    print("Your bmi is: ",bmi," and you are Overweight")
elif bmi>=30:
    print("Your BMI is: ",bmi," and you fall in obes catagory")
else:
    print("Enter valid values")
print("Thank You For Using Me")