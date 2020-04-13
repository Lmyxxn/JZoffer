def Find(matrix, number):
    if not matrix: return False
    rows = len(matrix)
    columns = len(matrix[0])
    if rows ==1 or columns == 1: return False
    m = 0
    n = columns -1
    while m < rows and n >= 0:
        if matrix[m][n] == number:
            return True
        elif matrix[m][n] > number:
            n -= 1
        elif matrix[m][n] < number:
            m += 1
    return False

print (Find([[1,2,3],[2,4,7],[3,6,9]], 5))
print (Find([[1,2,3],[2,4,7],[3,6,9]], 7))
