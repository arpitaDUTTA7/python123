#Program to find the Cube of elements up to a given Number in python:-

def cube(n):
    cubes={}
    for i in range(1,n+1):
        cubes[i]=i**3
    return cubes
x=int(input("Enter the number : "))
print(cube(x))