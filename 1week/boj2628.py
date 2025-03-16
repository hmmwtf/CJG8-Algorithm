width, height = map(int, input().split())

n = int(input())

row, col = [], []
row_side, col_side = [], []
row.append(0)
row.append(width)
col.append(0)
col.append(height)

for i in range(n):
    line, num = map(int, input().split())
    if line == 0:
        col.append(num)
    else:
        row.append(num)

row.sort()
col.sort()

for i in range(0, len(row)-1):
        row_side.append(row[i+1]-row[i])

for i in range(0, len(col)-1):
        col_side.append(col[i+1]-col[i])

print(max(row_side) * max(col_side))