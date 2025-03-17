# 파이썬 순열 (조합을 이용하기)
"""
from itertools import combinations

arr = [] 
for i in range(9):
    arr.append(int(input()))

for num in list(combinations(arr, 7)):
    if sum(num) == 100:
        for shorted in sorted(num):
            print(shorted)
        break
"""

arr = []

for i in range(9):
    arr.append(int(input()))

total = sum(arr)

solved = False

for i in range(len(arr)):
    fake1 = arr[i]
    for j in range(len(arr)):
        if i == j:
            continue
        else:
            fake2 = arr[j]
            for k in range(len(arr)):
                if total - fake1 - fake2 == 100:
                    arr.remove(fake1)
                    arr.remove(fake2)
                    solved = True
                    break
        if solved == True:
            break
    if solved == True:
        break               

arr.sort()
for i in range(7):
    print(arr[i])