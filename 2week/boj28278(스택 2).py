import sys

input = sys.stdin.readline

def one(arr, val):
    arr.append(val)
    return 

def two(arr):
    if len(arr) == 0:
        return -1
    else:
        return arr.pop()
    
def three(arr):
    return len(arr)

def four(arr):
    if len(arr) == 0:
        return 1
    else:
        return 0
    
def five(arr):
    if len(arr) == 0:
        return -1
    else:
        return arr[-1]
    
n = int(input().strip())
stack = []
for i in range(n):
    order = input().strip().split()
    cmd = order[0]
    if cmd == '1':
        one(stack, order[1])
    elif cmd == '2':
        print(two(stack))
    elif cmd == '3':
        print(three(stack))
    elif cmd == '4':
        print(four(stack))
    elif cmd == '5':
        print(five(stack))
    else:
        print("Invalid Input")
