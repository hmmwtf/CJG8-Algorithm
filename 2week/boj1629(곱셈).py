import sys
input = sys.stdin.readline

def mod_pow(a, b, mod):
    if b == 0:
        return 1
    temp = mod_pow(a, b // 2, mod)
    temp = (temp * temp) % mod
    if b % 2 == 0:
        return temp
    else:
        return (temp * a) % mod
a,b,c = map(int, input().strip().split())
print(mod_pow(a, b, c))