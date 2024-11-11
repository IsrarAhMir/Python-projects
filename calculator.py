def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("This is a Simple Calculator!")
    
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Input: Get the operation choice from the user
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter the operation (1/2/3/4): ")

    # Perform the calculation based on the user's choice
    if operation == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif operation == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif operation == '3':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif operation == '4':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid operation choice!")

if __name__ == "__main__":
    main()