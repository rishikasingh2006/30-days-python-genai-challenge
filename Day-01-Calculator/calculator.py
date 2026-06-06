print("=====SIMPLE CALCULATOR=====")
print("Addition")
print("Subtraction")
print("Multiplication")
print("Division")
 
choice = int(input("enter your choice :"))

a = float(input("enter your num1:"))
b = float(input("enter your num2:"))

if choice == 1:
    print("Result", a + b)
    
elif choice == 2:
     print("Result", a - b)
     
elif choice == 3:
     print("Result", a*b)

elif choice == 4:
    if b != 0:
        print("Result =", a / b)
    else:
        print("Division by zero not possible")

else:
    print("Invalid Choice")
