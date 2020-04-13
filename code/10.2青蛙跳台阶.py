# -*- coding:utf-8 -*-

def jumpFloor(number):
    if number == 0: return 0
    if number == 1:return 1
    if number == 2: return 2
    temp = 1
    res = 2
    for i in range(number-2):
        temp1 = res
        res = temp+res
        temp = temp1
    return res


print (jumpFloor(4))