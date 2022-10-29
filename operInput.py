a = int(input("Enter 1st num: "))
b = int(input("Enter 2nd num: "))
op = str(input("Choose a math operator(+, -, *, /): "))
if op == "+" :
  print(a+b)
elif op == "-" :
  print(a-b)
elif op == "*" :
  print(a*b)
elif op == "/" :
  print(a/b)
else :
  print("Invalid operator")