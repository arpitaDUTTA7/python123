def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
n=int(input("Enter the numbers of terms: "))
print("Fibonacci series:")
for i in range(n):
    print(fibonacci(i))
fibonacci(n)