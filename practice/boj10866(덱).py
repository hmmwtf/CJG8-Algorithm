import sys
from collections import deque

input = sys.stdin.readline

def push_front(q, x):
    q.appendleft(x)
    return

def push_back(q, x):
    q.append(x)
    return

def pop_front(q):
    if len(q) <= 0:
        return -1
    else:
        return q.popleft()
    
def pop_back(q):
    if len(q) <= 0:
        return -1
    else:
        return q.pop()

def size(q):
    return len(q)

def empty(q):
    if len(q) == 0:
        return 1
    else:
        return 0

def front(q):
    if empty(q):
        return -1
    else:
        return q[0]
    
def back(q):
    if empty(q):
        return -1
    else:
        return q[-1]

n = int(input().strip())
q = deque()

for _ in range(n):
    orders = list(input().strip().split())
    order = orders[0]
    
    if order == "push_back" or order == "push_front":
        value = int(orders[1])
        if order == "push_back":
            push_back(q, value)
        if order == "push_front":
            push_front(q, value)
    
    if order == "pop_front":
        print(pop_front(q))
    if order == "pop_back":
        print(pop_back(q))
    if order == "size":
        print(size(q))
    if order == "empty":
        print(empty(q))
    if order == "front":
        print(front(q))
    if order == "back":
        print(back(q))
    