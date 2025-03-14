def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiple(a, b):
    return a * b

def divide(a, b):
    return int(a / b)

def remain(a, b):
    return a % b

arr = input().split()
a, b = int(arr[0]), int(arr[1])
print(add(a,b))
print(minus(a,b))
print(multiple(a,b))
print(divide(a,b))
print(remain(a,b))