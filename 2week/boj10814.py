import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    info = input()
    result = []
    valid = True
    for j in range(len(info)):
        if info[j] == '(':
            result.append(info[j])
        elif info[j] == ')':
            try:
                result.pop()
            except IndexError:
                valid = False
                break
    if len(result) == 0 and valid:
        print("YES")
    else:
        print("NO")