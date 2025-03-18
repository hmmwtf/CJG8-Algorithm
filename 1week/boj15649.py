import itertools

n, m = map(int, input().split())

num = [ i for i in range(1, n+1)]

arr = itertools.permutations(num, m)

for i in arr:
    for j in i:
        print(j, end = ' ')
    print()


"""
def NandM (n, m):
    if m == n:
        return m
    print(m)

    return NandM(n, m+1)

n, m = map(int, input().split())
"""