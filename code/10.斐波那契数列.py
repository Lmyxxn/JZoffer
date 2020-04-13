def Fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    temp = 0
    res = 1
    for i in range(n-1):
        temp1 = res
        res = temp + res
        temp = temp1
    return res

print(Fibonacci(5))


