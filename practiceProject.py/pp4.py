# Fibonacci series
n = int(input("Enter the last term: "))
t1 = 0
t2 = 1 
if n == 1: 
   print(t1,end="\n")

else:
    print(t1,end="\n")
    print(t2,end="\n")
    for i in range(2,n):
       t=t1+t2
       print(t)
       t1=t2
       t2=t
       i+=1




