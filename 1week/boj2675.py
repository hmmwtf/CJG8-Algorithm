c = int(input())

for i in range(c):
    arr = input().split()
    r = int(arr[0])
    s = arr[1]
    result =""
    for j in range(len(s)):
        result += s[j] * r
    print(result)