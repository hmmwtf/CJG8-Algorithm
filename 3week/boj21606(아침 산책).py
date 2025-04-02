import sys
sys.setrecursionlimit(10**6)  # 재귀 호출의 최대 깊이를 늘려줍니다. 깊은 DFS를 위해 필요한 설정입니다.

N = int(input())  # 노드의 수를 입력받습니다.
inside = '0' + input()  # 각 노드가 실내(1)인지 실외(0)인지 저장한 문자열. 인덱스 맞추기 위해 앞에 '0'을 추가합니다.
graph = [[] for _ in range(N + 1)]  # 인접 리스트 형태로 그래프를 초기화합니다.
visited = [False] * (N + 1)  # 방문 여부를 체크할 리스트를 초기화합니다.
total = 0  # 경로의 개수를 저장할 변수입니다.

# 간선 정보를 입력받고 그래프를 구성합니다.
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())  # 간선의 두 정점 a, b를 입력받습니다.
    graph[a].append(b)  # a와 b를 인접 리스트에 추가합니다.
    graph[b].append(a)  # 무방향 그래프이므로 양쪽에 추가합니다.

    # 두 정점 모두 실내이면 경로의 수를 2 증가시킵니다.
    if inside[a] == "1" and inside[b] == "1":
        total += 2

def DFS(start):
    stack = [start]  # DFS를 위한 스택을 초기화합니다.
    visited[start] = True  # 시작 노드를 방문 처리합니다.
    inside_count = 0  # 현재 노드와 인접한 실내 노드 개수를 저장할 변수입니다.

    # 스택이 빌 때까지 반복합니다.
    while stack:
        node = stack.pop()  # 스택에서 노드를 하나 꺼냅니다.
        
        # 현재 노드의 인접 노드들을 탐색합니다.
        for v in graph[node]:
            # 인접한 노드가 실내라면
            if inside[v] == '1':
                inside_count += 1  # 실내 노드 개수를 증가시킵니다.
            
            # 인접한 노드가 실외이고 아직 방문하지 않았다면
            elif not visited[v] and inside[v] == "0":
                visited[v] = True  # 방문 처리
                stack.append(v)  # 스택에 추가하여 다음에 탐색하도록 합니다.

    return inside_count  # 현재 노드와 인접한 실내 노드 개수를 반환합니다.

# 모든 노드를 순회하면서 DFS를 실행합니다.
for i in range(1, N + 1):
    # 현재 노드가 실외이고 방문하지 않았다면 탐색 시작
    if inside[i] == '0' and not visited[i]:  
        result = DFS(i)  # DFS를 통해 인접한 실내 노드 개수를 계산합니다.
        total += (result) * (result - 1)  # 경로의 개수를 추가합니다.

print(total)  # 최종 결과를 출력합니다.