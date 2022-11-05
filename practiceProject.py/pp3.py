# Using a for loop and .append() method append each item with a Dr. prefix to the list.
# list1=["Phil","Oz","Seuss","Dre"]


list1=["Phil","Oz","Seuss","Dre"]
str="Dr."
newlist1=[str + i for i in list1]
print(newlist1)

# list2=[]
# list2=[i for i in input("Enter the list items:").split()]
# print(list2)
# string1=str(input("Enter the item to be added to the prefix:"))
# string2=str(input("Enter the item to be added to the suffix:"))
# newlist_2=[string1 + j for j in list2]
# newlist2_=[j+string2 for j in list2]
# print(newlist_2)
# print(newlist2_)
