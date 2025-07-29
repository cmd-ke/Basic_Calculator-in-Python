#Basic Calculator Program 
while True:
#Ask for the first number 
    num1 = float(input("enter the first number: "))
#Ask for the second number 
    num2 = float(input("enter the second number: "))
#Ask for the operation
    operation = input("input the operation: ")
    if operation == "+":
        result = num1 + num2
        print(result)
    elif operation == "-":
        result = num1 - num2
        print (result)
    elif operation == "x":
        result = num1 * num2
        print(result)
    elif operation == "*":
        result = num1 * num2
        print(result)
    elif operation == "**":
        result = num1 ** num2
        print(result)
    elif operation == "-":
        result = num1 - num2
        print(result)
    elif operation == "/":
        if num2 > 0:
            result = num1/num2
            print(result)
        else:
            print("You cannot divide by zero")
    else:
        print("enter a valid operation")

    response = input("Do you want to run another operation? (yes/no)").lower()

    if response != "yes":
        print("im worried to watch you leave Goodbye")
        break



