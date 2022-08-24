"""
Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year

"""

x = int(input("Enter a year: "))
print()

match x:
    case x:
        if  x % 100 != 0 and x % 4 == 0:
            print("Non century leap year")
            print()
        elif x % 100 == 0 and x % 400 == 0:
            print("Century leap year")
            print()
        elif x % 100 != 0 and x % 4 != 0:
            print("Non century non leap year")
            print()
        elif x % 100 == 0 and x % 4 != 0:
            print("Century non leap year")
            print()
