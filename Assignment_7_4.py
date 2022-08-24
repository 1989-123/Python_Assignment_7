""" Write a program which takes user’s age and display the category of person.
Agebelow 10 years- Kid, Age below 20 - Teen, Age below 40 - young,
Age below 60 -Experienced, Age above or equal 60 - Senior Citizen. """

x = int(input("Enter your age: "))

match x:
    case a:
        if x < 10:
            print("You\'re a Kid")
        elif x < 20:
            print("You\'re a Teen")
        elif x < 40:
            print("You\'re a Young")
        elif x < 60:
            print("You\'re a Experienced")
        elif x > 60 or x == 60:
            print("You\'re a senior Citizen")
