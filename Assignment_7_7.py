""" Write a python program to check whether a given number is positive
negative or zero using match case statement """

x = int(input("Enter a number: "))
print()

match x:
    case x:
        if x > 0:
            print("Number is positive")
            print()
        elif x < 0:
            print("Number is negative")
            print()
        elif x == 0:
            print("Number is zero")
            print()
