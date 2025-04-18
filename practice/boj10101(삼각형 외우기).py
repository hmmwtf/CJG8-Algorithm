import sys

input = sys.stdin.readline

a = int(input().strip())
b = int(input().strip())
c = int(input().strip())

if (a+b+c) == 180:
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a== c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")