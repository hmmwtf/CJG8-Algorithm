arr = input()
n = int(arr)

cnt = 0
result = 0

if n < 100:
    result = n
else:
    for i in range(100, n+1):
        x = i // 100
        y = int((i /10) % 10)
        z = i % 10
        if y - x == z - y:
            cnt += 1
    result = 99 + cnt

print(result)