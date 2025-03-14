arr = []
idx = 0
for i in range(9):
    num = int(input())
    arr.append(num)

for i in range(9):
    if max(arr) == arr[i]:
        idx = i

print(max(arr))
print(idx+1)