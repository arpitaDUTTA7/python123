# defining a function
#  def hello():
#     print("Hello World")
#     print("Hello Mars")

# calling a function
#  hello()

# using parameters and arguments
# def add(num1,num2):     #parameters num1 and num2 when defining a function
#     sum=num1+num2
#     print(sum)
# add(4,5)                #arguments 4 and 5 are passed to parameters when calling a function

# def sub(a,b):
#     difference=a-b
#     print(difference)
# sub(67,49)

# def multiply(x,y):
#     product=x*y
#     return (product)
# p=multiply(6.8,4.5)
# print("{:.2f}".format(p))

def name(firstname,lastname):
    print("My name is",firstname+" "+lastname)
name("Arpita","Dutta")

def fruits(*args):
    print(args)
    print(*args)
    print(args[3])
    print(*args[3])
fruits("apple","orange","mango","banana","cherry")

def cars(cars,*args):
    print(cars)
    print(args)
cars("BMW","Audi","Mercedes")