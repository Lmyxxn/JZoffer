#时间O(N),空间O(1)（在python中，字符串是不可变的，参考剑指的做法做的话，这里需要开一个数组,假装空间还是O（1））
#其实可以直接通过切片操作做
def ReplaceBlank(str1):
    if str1 == '': return
    str_ = list(str1)
    n = len(str_)
    count = 0
    for i in str_:
        if i == ' ':
            count += 1
    str_ += ' '*(count)*2
    p = n-1
    q = len(str_)-1
    while p >= 0:
        if str_[p] != ' ':
            str_[q] = str_[p]
            p -=1
            q -= 1
        else:
            str_[q] = '0'
            str_[q-1] = '2'
            str_[q-2] = '%'
            p -= 1
            q -= 3
    return ''.join(str_)

# print(ReplaceBlank('hello world'))
print(ReplaceBlank(' '))
print(ReplaceBlank('   '))
print(ReplaceBlank(''))



#直接切片 #时间O(N),空间O(1)
def ReplaceBlank(str1):
    for i in range(len(str1)):
        if str1[i] == ' ':
            str1 = str1[:i] + '%20' + str1[i+1:]
    return str1
# print(ReplaceBlank('hello world'))
print(ReplaceBlank(' '))

