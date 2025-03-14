def is_prime(n):
    if n < 2:
        return 0 
    else:
        cnt = 0
        for i in range(2, int(n**(0.5))+1):
            if n % i == 0:
                cnt += 1
        if cnt > 0:
            return 0
        else:
            return 1

t = int(input())

for i in range(t):
    num = int(input())
    a , b = int(num / 2), int(num / 2)
    while(True):
        if is_prime(a) == 1 and is_prime(b) == 1:
            break
        a -= 1
        b += 1
    print(a, b)