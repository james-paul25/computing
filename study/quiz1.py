# making functions

# example of recursive function
def fibo(n):
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)

print("The value for fib or 0 is: ", fibo(4))