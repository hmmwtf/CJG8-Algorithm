import sys

input = sys.stdin.readline

n = int(input().strip())
member = []

for _ in range(n):
    age, name = input().strip().split()
    age = int(age)
    member.append((age, name))
    
member.sort(key=lambda member : member[0])

for age, name in member:
    print(age, name)