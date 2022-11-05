# Fibonacci series
n = int(input("Enter the last term: "))
t1 = 0
t2 = 1 
print("0",end="\n")
print("1",end="\n")
for i in range(2,n):
    t=t1+t2
    print(t)
    t1=t2
    t2=t
    i+=1




