import sys
input = sys.stdin.readline

sen = input().rstrip()
stack = []
total = 0
temp = 1

for i in range(len(sen)):
    if sen[i] == '(':
        stack.append(sen[i])
        temp *= 2
    elif sen[i] == '[':
        stack.append(sen[i])
        temp *= 3
    elif sen[i] == ')':
        if not stack or stack[-1] != '(':
            total =0
            break
        if sen[i-1] == '(':
            total += temp
        stack.pop()
        temp //= 2
    elif sen[i] == ']':
        if not stack or stack[-1] != '[':
            total = 0
            break
        if sen[i-1] == '[':
            total += temp
        stack.pop()
        temp //= 3
    
if stack:
    print(0)
else:
    print(total)