"""
import sys
from collections import Counter

input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().strip().split()))
m = int(input().strip())
b = list(map(int, input().strip().split()))

count = Counter(a)

result = []
for num in b:
    result.append(str(count[num]))
    
print(" ".join(result))
"""

import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input().strip())
cards = sorted(list(map(int, input().split())))
m = int(input().strip())
queries = list(map(int, input().split()))

result = []
for query in queries:
    left_index = bisect_left(cards, query)   
    right_index = bisect_right(cards, query) 
    result.append(str(right_index - left_index))  

print(" ".join(result))