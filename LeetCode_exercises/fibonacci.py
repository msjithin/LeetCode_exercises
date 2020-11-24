

dict={1:1, 2:2}
def fib(n):
    # this one is quite slow for numbers larger then 20
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return fib(n-1)+fib(n-2)

def fibonacci(num, dict):
    # quite efficient and fast - we save values once they are calculated.
    if num in dict:
        return dict[num]
    else:
        ans = fibonacci(num-1, dict)+fibonacci(num-2, dict)
        dict[num]=ans
        return ans

def factorial(num, dict):
    if num in dict:
        return dict[num]
    else:
        ans = num * factorial(num-1, dict)
        dict[num]=ans
        return ans

