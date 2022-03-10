print('checking triangle')

a = int(input("enter number1:\n"))
b = int(input("enter number2:\n"))
c = int(input("enter number3:\n"))
if a==0 or b==0 or c==0 :
    print('please enter a valid number')
if a+b>c and a+c>b and b+c>a:
 print("this is a triangle")
else:
 print("this is not triangle")