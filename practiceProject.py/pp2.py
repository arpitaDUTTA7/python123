 # for in list
cars = ["Nano", "Ford", "Tata", "BMW", "Thar"]
for i in cars:
      if i == "Tata":
          break
      print(i)

fruits = ["Apples", "Oranges", "Mangoes", "Cherries", "Bananas"]
for i in fruits:
    if i == "Oranges":
        continue
    print(i)

 # for in string
for i in "Hello World":
     print(i) 

for i in range(4,11,2):
    print(i)

for i in range(6):
    if i == 3:
      break
    print(i)
else:
        print("Loop over")

# Nested loops
colors = ["Red", "Blue", "Black"]
cars = ["Nano", "Tata", "Ford"]

for i in colors:
    for j in cars:
        print(i,j)