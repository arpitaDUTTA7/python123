# Factorial of a number
n = int(input("Enter the number: "))
f=1
for i in range(n,1,-1):
    f=f*i
print("Factorial of",n,"is =",f)