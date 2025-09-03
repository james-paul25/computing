# making functions

# example of recursive function
def fibo(n = 1):
    if n <= 1:
        return n
    else:
        return fibo(fibo(n - 1) + fibo(n - 2))
    
n = 3
for i in range(n):
    print(fibo(i))