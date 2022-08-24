""" Write a python program to check whether a given string is a multiword
string or single word string using match case statement """

x = "Ja"
y = x.__len__()
print()

match y:
    case y:
        if y == 1:
            print("Single word string")
            print()
        else:
            print("Multiword string")
            print()
