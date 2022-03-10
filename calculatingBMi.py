

print('Calculating BMI')
weight = float(input('Please Enter Your Weight In Kilo:'))
height = float(input('Please Enter Your height In cm:'))

if(weight == 0 or height == 0):
    print('Enter Valid Number')
else:
    bmi = (weight/height**2)*10000
    print('Your BMI Is', bmi)
if bmi<18.5:
 print("you are Underweight")
elif 18.5<=bmi<=24.9:
 print("you are  Normal")
elif 25<=bmi<=29.9:
 print("you are Overweight")
elif 30<=bmi<=34.9:
 print("you are  Obese")
elif 35<=bmi:
 print("you are Extremely Obese")