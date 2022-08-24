"""
Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday

"""

fav_colour = input("Enter your favorite color: ")
print()

match fav_colour:
    case "yellow":
        print("Today is monday")
        print()
    case "blue":
        print("Today is tuesday")
        print()
    case "orange":
        print("Today is wednesday")
        print()
    case "white":
        print("Today is thursday")
        print()
    case "black":
        print("Today is friday")
        print()
    case "red":
        print("Today is saturday")
        print()
    case _:
        print("Today is sunday")
        print()
