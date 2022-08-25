print("***TO PERFORM THE 6 OPERATION IN A CALCULATOR")


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y



def divide(x, y):
    return x / y


def Square(x):
    return  x*x


print("Please Choose an option")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5. Square")
print("6. Invalid value")

while True:

    choice = input("Enter choice(1/2/3/4/5): ")

   #you can chooese the number as per operation you want
    if choice in ('1', '2', '3', '4','5'):
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

        elif choice == '5':
            print(num1, "*", num1, "=", Square(num1))



        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")