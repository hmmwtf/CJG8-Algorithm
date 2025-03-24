import sys

input = sys.stdin.readline

n = int(input().strip())

solutions = list(map(int, input().strip().split()))
solutions.sort()

left, right = 0, n - 1
# 두 수의 합을 일단 최대값으로 고정
best_sum = sys.maxsize
result_left, result_right = solutions[left], solutions[right]

# 투포인터 사용
while left < right:
    current = solutions[left] + solutions[right]
    
    if abs(current) < best_sum:
        best_sum = abs(current)
        result_left, result_right = solutions[left], solutions[right]
        
    if current < 0:
        left += 1
    elif current > 0:
        right -= 1
    else:
        break
    
print(result_left, result_right)