"""
from itertools import permutations

def sidemax(arr):
    l = len(arr)
    total = 0
    for i in range(len(arr)-1):
        first = arr[i]
        second = arr[i+1]
        total += abs(first - second)
    return total

n = int(input())

arr = list(map(int, input().split()))
resultsides = []

for sidesum in list(permutations(arr)):
    resultsides.append(sidemax(sidesum))

print(max(resultsides))
"""