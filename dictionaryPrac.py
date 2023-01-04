# Dictionaries are used to store data values in key value pair
#Dictionaries are ordered
myDictionary={"name":"Arpita","age":19,"rollno":20,"percentage":float(91)}
a=myDictionary["name"]
b=myDictionary.get("percentage")
print(a)
print(b)
print(myDictionary)
print(len(myDictionary))
c=myDictionary.keys()     # List will be printed
print(c)
d=myDictionary.values()   # List will be printed
print(d)
e=myDictionary.items()    # List of tuples will be printed
print(e)    
#myDictionary["age"]=22
myDictionary.update({"age":22})
print(myDictionary)
#myDictionary.pop("rollno")
#print(myDictionary)

print("Dictionary keys are:")
for i in myDictionary.keys():
    print(i)
print("Dictionary values are:")
for j in myDictionary.values():
    print(j)
 