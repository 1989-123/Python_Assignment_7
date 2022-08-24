print("Enter three numbers: ")
a, b, c = int(input()), int(input()), int(input())
print()
print("1. Set of three numbers are lengths of an isosceles triangle or not")
print("2. Set of three numbers are lengths of sides of a right angled triangle or not")
print("3. Set of three numbers are equilateral triangle or not ")
print()

x = int(input("Enter your choice: "))
match x:
    case 1:
        if a == b or b == c or c == a:
            print("Length of an isosceles triangle")
        else:
            print("Not an isosceles triangle")
    case 2:
         t = a * a + b * b
         t1 = c * c;
         if t == t1:
            print("Triangle is right angled triangle")
         else:
            print("Triangle is not right angled triangle")
    case 3:
        if a == b and b == a:
            print("Equilateral triangle")
        else:
            print("Not equilateral triangle")
