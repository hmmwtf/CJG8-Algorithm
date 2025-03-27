import sys
input = sys.stdin.readline

while True:
    sen = input().rstrip()
    
    if sen == '.':
        break
    
    stack = []
    
    flag = True
    
    for i in range(len(sen)):
        if sen[i] == '(':
            stack.append(sen[i])
        elif sen[i] == '[':
            stack.append(sen[i])
        elif sen[i] == ')':
            if not stack or stack[-1] != '(':
                flag = False
                break
            stack.pop()
        elif sen[i] == ']':
            if not stack or stack[-1] != '[':
                flag = False
                break
            stack.pop()
            
    if flag and not stack:
        print("yes")
    else:
        print("no")