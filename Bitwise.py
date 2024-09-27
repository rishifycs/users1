def get_binary_input(prompt):
    number = int(input(prompt))
    return number

def main():
    num1 = get_binary_input("Enter the first number: ")
    num2 = get_binary_input("Enter the second number: ")

    print(f"First number in binary: {bin(num1)}")
    print(f"Second number in binary: {bin(num2)}")

    print("\nChoose a bitwise operation:")
    print("1. AND (&)")
    print("2. OR (|)")
    print("3. XOR (^)")
    print("4. NOT (~)")

    operation = int(input("Enter the number of the operation you want to perform: "))

    if operation == 1:
        result = num1 & num2
    elif operation == 2:
        result = num1 | num2
    elif operation == 3:
        result = num1 ^ num2
    elif operation == 4:
        result = ~num1
        print(f"Result of NOT operation on first number in binary: {bin(result)}")
        print(f"Result of NOT operation on first number in decimal: {result}")
        return
    else:
        print("Invalid operation selected.")
        return

    print(f"Result in binary: {bin(result)}")
    print(f"Result in decimal: {result}")

if __name__ == "__main__":
    main()
