import sys

input = sys.stdin.readline
"""
def quick_sort(arr):
    l = len(arr)
    if l <= 1:
        return arr
    pivot = arr[l//2]
    pl, mid, pr = [], [], []
    for num in arr:
        if num < pivot:
            pl.append(num)
        elif num > pivot:
            pr.append(num)
        else:
            mid.append(num)
    
    return quick_sort(pl) + mid + quick_sort(pr)
"""
n = int(input())

cnt_arr = [ 0 for i in range(10001)]

for i in range(n):
    cnt_arr[int(input())] += 1         

for i in range(len(cnt_arr)):
    if cnt_arr[i] > 0:
        for j in range(cnt_arr[i]):
            print(i)