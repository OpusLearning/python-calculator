def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    return x ** 0.5


print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Square_root")

choice = input("Enter choice(1/2/3/4/5/6): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
<<<<<<< HEAD
elif choice == '5':
    print(num1, "**", num2, "=",  power(num1, num2))
elif choice == '6':
    print(num1, "/", num2, "=", Square_root(num1, num2))
=======
elif choice == "5":
    print(num1, "**", num2, "=", power(num1,num2))
elif choice == "6":
    print(num1, "root", num2, "=", square_root(num1,num2))
>>>>>>> feature-advanced-calc

else:
    print("Invalid Input")

