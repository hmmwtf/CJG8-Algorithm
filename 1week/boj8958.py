t= int(input())

for i in range(t):
    score = 0
    num = 0
    c = input()
    l = len(c)
    for j in range(l):
        if c[j] == "O":
            num += 1
            score = score + num
        else:
            num = 0
    print(score)
