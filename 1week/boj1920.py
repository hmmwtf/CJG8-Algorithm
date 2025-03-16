n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

result = [0 for i in range(n)]

a_set = set(a)
for x in b:
    if x in a_set:
        print(1)
    else:
        print(0)