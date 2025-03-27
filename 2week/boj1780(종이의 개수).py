import sys
input = sys.stdin.readline

def count_papers(x, y, size):
    global minus_one_count, zero_count, one_count
    first_value = paper[x][y]
    is_same = True

    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != first_value:
                is_same = False
                break
        if not is_same:
            break

    if is_same:
        if first_value == -1:
            minus_one_count += 1
        elif first_value == 0:
            zero_count += 1
        else:
            one_count += 1
    else:
        new_size = size // 3
        for i in range(3):
            for j in range(3):
                count_papers(x + i * new_size, y + j * new_size, new_size)

n = int(input().strip())
paper = [list(map(int, input().strip().split())) for _ in range(n)]

minus_one_count = 0
zero_count = 0
one_count = 0

count_papers(0, 0, n)

print(minus_one_count)
print(zero_count)
print(one_count)
