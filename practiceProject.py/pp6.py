# WAP to use loop to find the factorial of a given number.
n = int(input("Enter the number: "))
f=1
for i in range(n,1,-1):
    f=f*i
print("Factorial of",n,"is =",f)