#数学归纳法可得 第n阶台阶总方法为2**(n-1)
def jumpFloor(number):
    if number == 0: return 0
    if number == 1:return 1
    if number == 2: return 2
    res = 2
    for i in range(3,number+1):
        res = res * 2
    return res

print (jumpFloor(4))
