colors = ["Red","Blue","White","Black",20]
#cars = ("BMW","Mercedes","Tesla")
#print(colors[1:4])
#colors[2]="Green"
#print(colors)
#colors[0:2]=["Orange","Yellow"] 
#colors.insert(2,"Indigo")
#colors.append("Purple")
#print(colors)
#colors.extend(cars)
#print(colors) 
#colors.remove("Black")
#colors.pop(1)   #pop removes from a specific index
#print(colors)
#colors.clear()   #del colors[0]
#print(colors)


#for x in colors:
#    print(x)

#for y in range(len(colors)):
#    print(y)

#x=0
#while x < len(colors):
#    print(colors[x])
#    x+=1

cars=["TATA","NANO","ALTO","JEEP"]

'''
newlist=[]
for i in cars:
    if "A" in cars:
        newlist.append(i)
print(newlist)
'''

newlist=[x.lower() for x in cars]
#newlist = [x for x in cars if x != "TATA"]
#    expression  item  list  condition
print(newlist)

numbers=[1,4,6,2,10]

numbers.reverse()
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

num=[1,2,3,4,5]
newlist=[x**2 for x in num]
print(newlist)

n=[1,2,3,4,5,2,6]
#in the above list, find value 2, if it is present, replace it with 200, only update the first occurance
#for i in n:
#    if i == 2:
#       a=n.index(i)
#        n.pop(n.index(2))
#        n.insert(a,200)
#       break
#print(n)

indx= n.index(2)
n[indx]=200
print(n)

m=n.copy()
print(m)

l=list(n)
print(l)


list1=["x","y","z"]
list2=[1,2,3]
list3 = list1 + list2   #can only concatenate list (not tuple) to list
print(list3)   
#for i in list1:
#    list2.append(i)
#print(list2)

#for i in list2:
#    list1.append(i)
#print(list1)

list1.extend(list2)
print(list1)