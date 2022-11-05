# Write a pattern to print the following number patterns using a loop.
# a) 1
#    1  2
#    1  2  3
#    1  2  3  4  5

# b) 5  4  3  2  1
#    4  3  2  1
#    3  2  1
#    2  1
#    1


# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#    for j in range(1,i+1):
#       print(j,end=" ")
#    print(" ")

r=int(input("Enter the number of rows: "))
for a in range(0,r+1):
    for b in range(r-a,0,-1):
        print(b,end=" ")
    print(" ")