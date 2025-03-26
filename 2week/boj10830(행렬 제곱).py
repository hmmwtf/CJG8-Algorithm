import sys

input = sys.stdin.readline

n, b = map(int, input().strip().split())
matrix = [list(map(int, input().strip().split())) for _ in range(n)]

# 직접 짠 거(시간 복잡도 생각 X)
"""
result =[[1 if i == j else 0 for i in range(n)] for j in range(n)]

def matrix_mul(a, b, mod = 1000):
    n = len(a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            sum = 0
            for k in range(n):
                sum += a[i][k] * b[k][j]
                sum %= mod
            result[i][j] = sum
    return result

for _ in range(b):
    result = matrix_mul(result, matrix)
    
for row in result:
    print(' '.join(map(str, row)))
"""

# 분할 정복
def matrix_multiply(a, b, mod=1000):
    n = len(a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = sum(a[i][k] * b[k][j] for k in range(n)) % mod
    return result

def matrix_power(matrix, exponent, mod=1000):
    n = len(matrix)
    # 단위 행렬 
    result = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
    while exponent > 0:
        if exponent % 2 == 1:
            result = matrix_multiply(result, matrix, mod)
        matrix = matrix_multiply(matrix, matrix, mod)
        exponent //= 2
    
    return result

result = matrix_power(matrix, b)

for row in result:
    print(' '.join(map(str, row)))
