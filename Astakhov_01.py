def check_pos(a, b, c, check):
    if(a + b > c and a + c > b and b + c > a):
        print("This triangle can be drawn")
    else:
        print("This triangle doesn't exist")
        check = 1
    return check

def triangle_defin(a, b, c):
    if(pow(a, 2) + pow(b, 2) == pow(c, 2) or pow(a, 2) + pow(c, 2) == pow(b, 2) or pow(b, 2) + pow(c, 2) == pow(a, 2)):
        print("Triangle is right")
    if(a == b and b == c and a == c):
        print("Triangle is equilateral")
    elif(a == b or a == c or b == c):
        print("Triangle is isosceles")
    else:
        print("Triangle is versatile")
    
print("Triangle check\n")
check = 0
a = int(input("Enter value of the first border: "))
if(a <= 0):
    raise Exception("Sorry, value of border might be more than zero")
b = int(input("Enter value of the second border: "))
if(a <= 0):
    raise Exception("Sorry, value of border might be more than zero")
c = int(input("Enter value of the third border: "))
if(a <= 0):
    raise Exception("Sorry, value of border might be more than zero")

print("\n")

if(check_pos(a, b, c, check) == 0):
    triangle_defin(a, b, c)
