import sys
from collections import Counter

input = sys.stdin.readline

def r_operation(matrix):
    new_rows = []
    max_len = 0

    for row in matrix:
        cnt = Counter(x for x in row if x != 0)
        pairs = sorted(cnt.items(), key=lambda x: (x[1], x[0]))
        new_row = []
        for num, freq in pairs:
            new_row.extend([num, freq])

        max_len = max(max_len, len(new_row))
        new_rows.append(new_row)

    max_len = min(max_len, 100)
    for i in range(len(new_rows)):
        if len(new_rows[i]) < max_len:
            new_rows[i].extend([0] * (max_len - len(new_rows[i])))
        else:
            new_rows[i] = new_rows[i][:max_len]

    return new_rows

def c_operation(matrix):
    transposed = [list(row) for row in zip(*matrix)]
    operated = r_operation(transposed)
    new_matrix = [list(row) for row in zip(*operated)]
    return new_matrix

def solve():
    r, c, k = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(3)]

    time = 0
    while True:
        if 0 <= r-1 < len(A) and 0 <= c-1 < len(A[0]) and A[r-1][c-1] == k:
            print(time)
            return

        if time > 100:
            print(-1)
            return

        if len(A) >= len(A[0]):
            A = r_operation(A)
        else:
            A = c_operation(A)

        time += 1

solve()