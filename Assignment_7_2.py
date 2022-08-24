x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print()
print("1. Addition")
print("2. Subtrction")
print("3. Multiplication")
print("4. Divsion")
print()
z = eval(input("Enter your choice: "))
print()

match z:
    case 1:
        print("Sum is:", x + y)
        print()
    case 2:
        print("Subtraction is:", x - y)
        print()
    case 3:
        print("Multiplication is:", x * y)
        print()
    case 4:
        print("Division is:", x / y)
        print()
    case _:
        print("Enter valid input")
        print()
