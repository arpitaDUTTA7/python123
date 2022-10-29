#Take an input from user,if the length of that input > 3 characters then add "ing" as suffix otherwise print the same input
a=str(input("Enter a word: "))
b=str("ing")
c=int(a.__len__())
if c>3:
  print(a+b)
else:
    print(a)