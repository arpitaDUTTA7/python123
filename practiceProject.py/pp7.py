# WAP to display all prime numbers within a range. Take the user input for start and end of range.
u=int(input("Enter the upper range value: "))
l=int(input("Enter the lower range value: "))
print("Prime numbers within the range are: ")
for n in range(u,l+1):
    if n>1:
      for i in range(2,n):
        if n % i == 0:
          break
      else:
        print(n)

