# Tuples store multiple items in a single variable
# Tuples are ordered
# Tuples are immutable
# Tuples allow duplicate values

mytuple = (1,2,3,4,5)
print(mytuple)

print(len(mytuple))

tuple1=("apple")
print(tuple1)
tuple2=("apple",)
print(tuple2)

tuple3=("car","bike","boat","jet")
print(tuple3[1:3])

list1=list(tuple3)
list1.append("cycle")
print(tuple(list1))
