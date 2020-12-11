# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight/height**2

if bmi > 35:
  print(f"your BMI is {round(bmi,2)}, you are clinically obese")
elif bmi > 30:
  print(f"your BMI is {round(bmi,2)}, you are obese")
elif bmi > 25:
  print(f"your BMI is {round(bmi,2)}, you are slightly overweight")
elif bmi > 18.5:
  print(f"your BMI is {round(bmi,2)}, you are normal weight")
else:
  print(f"your BMI is {round(bmi,2)}, you are underweight")