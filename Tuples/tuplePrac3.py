# tuple1 = (1,2,3)
# (one,two,three) = tuple1
# print(one)
# print(two)
# print(three)

tuple1 = ("car","bike","boat","cycle")
# (item1,*item2,item3)=tuple1               # using * when there is too many values to unpack
# print(item1)                              # * can contain n number of variables
# print(item2)
# print(item3)


(item1,*item2)=tuple1                     
print(item1)
print(item2)


# WAP to unpack following tuple into 4 variables
tuple2=(10,20,30,40)
# (a,b,c,d)=tuple2
# print(a)
# print(b)
# print(c)
# print(d)

# for i in tuple2:
#     print(i)

i=0
while i<len(tuple2):
     print(tuple2[i])
     i+=1

tuple3=tuple1+tuple2
print(tuple3)

# print(tuple1.count())       # read only
# print(tuple1.index())       # read only

tuple4=tuple2[1],tuple2[2]
print(tuple4)

tuple5=(10,20,30,20,40)
print(tuple5.count(20))

# name1=str(input())
# name2=str(input())
# name3=str(input())
# name4=str(input())
# tuple6=(name1,name2,name3,name4)
# print(tuple6)

tuple7=("H","E","L","L","O")
print(*tuple7)

for i in tuple7:
     print(i,end="")
