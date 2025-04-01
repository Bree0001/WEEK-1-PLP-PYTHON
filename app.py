num1 = float(input("Enter your first number here: "))
num2 = float(input("Enter your second number here: "))
operation = input("Choose the operation you want to perform here (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(num1, "+", num2, "=", result)
elif operation == "-":
    result = num1 - num2
    print(num1, "-", num2, "=", result)
elif operation == "*":
    result = num1 * num2
    print(num1, "*", num2, "=", result)
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(num1, "/", num2, "=", result)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation entered")
