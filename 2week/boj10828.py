def push(arr, val):
    arr.append(val)

def pop(arr):
    if len(arr) == 0:
        print(-1)
    else:
        print(arr[-1])
        arr.remove

def size(arr):
    print(len(arr))

def is_empty(arr):
    if len(arr) == 0:
        print(1)
    else:
        print(0)
    
def top(arr):
    if len(arr) == 0:
        print(-1)
    else:
        print(arr[-1])

n = int(input())
arr = []
for i in range(n):
    order = input().split()
    if order[0] == 'push':
        push(arr, order[1])
    elif order[0] == 'pop':
        pop(arr)
    elif order[0] == 'size':
        size(arr)
    elif order[0] == 'empty':
        is_empty(arr)
    elif order[0] == 'top':
        top(arr)
    else:
        print("Invalid Input")
