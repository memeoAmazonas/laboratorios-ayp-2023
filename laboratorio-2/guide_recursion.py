def sumNotRecursive(n):
    result= 0
    for i in range(n):
        result += i+1
    return result

def sumRecursive(n):
    if n <= 1:
        return n
    else:
        return n + sumRecursive(n-1)

print(sumRecursive(10))
print(sumNotRecursive(10))
