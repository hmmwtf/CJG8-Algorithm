def pluscycle(n):
    start = n
    cnt = 0
    while True:
        ten_digit = n // 10
        digit = n % 10

        sum_digit = ten_digit + digit

        newNum = digit * 10 + sum_digit % 10

        cnt += 1

        if newNum == start:
            return cnt
        n = newNum
        
num = int(input())
print(pluscycle(num))