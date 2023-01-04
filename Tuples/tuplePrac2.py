tuple1=(10,20,30,40,50)   # Reverse it
list1=list(tuple1)
list1.reverse()
print(tuple(list1))


tuple2=("Arpita",)         # Print as tuple not string
print(tuple2)

tuple3=("apple","orange","pineapple")
#list1=list(tuple3)
#list1.pop(2)
#print(tuple(list1))


tuple4=(1,2,3,[6,7],4,5)
print(tuple4[3][0])
list1=list(tuple4)
list1[3][0]=8
print(tuple(list1))

tuple5=(10,20)
tuple6=(30,40)
temp=tuple5 
tuple5=tuple6
tuple6=temp
print(tuple5)
print(tuple6)
