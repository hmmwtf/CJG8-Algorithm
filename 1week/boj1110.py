def plus_cycle(n):
    cnt = 0
    first = n

    while True:
        ten_digit = n // 10
        digit = n % 10

        sum_digit = (ten_digit + digit) % 10

        nextN = digit * 10 + sum_digit

        if first == nextN:
            cnt += 1
            break
        else:
            cnt += 1
        n = nextN
    return cnt

n = int(input())
print(plus_cycle(n))