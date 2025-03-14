def is_prime(n):
    if n < 2:
        return 0
    else:
        cnt = 0
        for i in range(2, int(n**(0.5)+1)):
            if n % i == 0:
                cnt += 1
        if cnt > 0:
            return 0
        else:
            return 1

n = int(input())
cnt = 0
arr = list(map(int,input().split()))
for i in arr:
    if is_prime(i) == 1:
        cnt += 1

print(cnt)