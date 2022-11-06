def n(*args):
    print((args))
n("Arpita","Dutta","19")

def vegetables(*args):
    for i in args:
        print(i)
vegetables("potato","tomato","carrot")

def name(firstname="Ben",age=100):
    print("My name is "+firstname,"and my age is",age)
name()
name("Mike",101)

def func(name,salary=10000):
    print(name," ",salary)
func("Andy",9000)
func("Tyler",8000)
func("Josh")

# arbitrary keyword arguments
def info(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)
info("Arpita",age=19,place="Assam",num=5555555555)
