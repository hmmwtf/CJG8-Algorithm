import sys

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a, b):
    return a * b / gcd(a, b)

input = sys.stdin.readline

n = int(input().strip())
for i in range(n):
    a, b = map(int, input().split())
    print(int(lcm(a, b)))