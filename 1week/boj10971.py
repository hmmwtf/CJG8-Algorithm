from itertools import permutations

n = int(input())
cost_matrix = [list(map(int, input().split())) for _ in range(n)]

min_cost = float('inf')

for perm in permutations(range(1, n)):
    route = [0] + list(perm) + [0]
    total_cost = 0
    valid = True
    for i in range(len(route) - 1):
        cost = cost_matrix[route[i]][route[i+1]]
        if cost == 0:
            valid = False
            break
        total_cost += cost
    if valid and total_cost < min_cost:
        min_cost = total_cost

print(min_cost)