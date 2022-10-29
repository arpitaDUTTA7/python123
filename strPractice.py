name = str(input("Enter a name: "))
print("First letter",name[0])
print("Second letter",name[-1])
i=int(name.__len__())
j=int(name.__len__()/2)
k=int(((name.__len__())+1)/2)
if i%2==0 :
   print("Middle letter",name[j])
else :
   print("Middle letter",name[k])