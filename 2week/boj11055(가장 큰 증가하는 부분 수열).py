import sys, bisect
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().strip().split()))

increse_num = []

for x in a:
    pos = bisect.bisect_left(increse_num, x)
    
    if pos == len(increse_num):
        increse_num.append(x)
    else:
        increse_num[pos] = x
        
print(sum(increse_num))