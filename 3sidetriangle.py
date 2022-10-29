a = int(input("Enter 1st side: "))
b = int(input("Enter 2nd side: "))
c  = int(input("Enter 3rd side: "))
if (a+b)>c or (b+c)>a or (c+a)>b:
    print("It is a triangle")
else:
    print("It is not a triangle")