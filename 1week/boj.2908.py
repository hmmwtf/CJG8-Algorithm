arr = input().split()

a, b = arr[0], arr[1]
ra, rb = int(a[::-1]), int(b[::-1])

print(max(ra, rb))