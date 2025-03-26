# 각 원을 나타내는 클래스 (원 정보와 자식 노드 리스트 포함)
class CircleNode:
    def __init__(self, x, r):
        self.x = x
        self.r = r
        self.left = x - r
        self.right = x + r
        self.children = []  # 이 원의 내부에 포함(또는 접)하는 원들

def build_tree(circles):
    # circles: 원 객체들의 리스트
    # 원들을 왼쪽 끝점 기준으로 정렬
    circles.sort(key=lambda c: c.left)
    root_nodes = []
    
    # 각 원을 순회하며 포함/접촉 관계에 따라 트리 구성 (간단한 방식의 pseudocode)
    for circle in circles:
        parent_found = False
        # 이미 트리에 있는 원들 중, 현재 원을 포함할 수 있는 가장 작은 원(적절한 부모)를 찾음
        for root in root_nodes:
            if root.left <= circle.left and circle.right <= root.right:
                # 부모 후보가 있다면, 재귀적으로 자식 노드 리스트에 삽입하는 함수를 호출
                insert_child(root, circle)
                parent_found = True
                break
        if not parent_found:
            root_nodes.append(circle)
    return root_nodes

def insert_child(parent, child):
    # 만약 부모의 자식 중, child를 포함할 수 있는 더 작은 원이 있다면 거기로 이동
    for sub in parent.children:
        if sub.left <= child.left and child.right <= sub.right:
            insert_child(sub, child)
            return
    # 그렇지 않으면, parent의 자식으로 child를 추가
    parent.children.append(child)

def count_regions(node):
    # node: CircleNode
    # 기본적으로, 하나의 원은 평면을 2개의 영역으로 분할한다.
    # 그러나 부모 내부에 여러 자식이 존재하면, 자식들 사이의 접점을 보정해야 함.
    # 여기서는 간단히, 각 노드는 1개의 추가 영역을 만든다고 가정.
    regions = 1  # 이 원이 추가하는 기본 영역
    for child in node.children:
        regions += count_regions(child) - 1  # 자식이 만드는 영역 중, 접점 보정 (중복 영역 제거)
    return regions

def total_regions(root_nodes):
    # 트리의 모든 루트 노드에 대해 계산하고, 외부 영역 1을 더함.
    regions = 0
    for root in root_nodes:
        regions += count_regions(root)
    return regions + 1

# 사용 예시:
# 입력 처리
import sys
input = sys.stdin.readline
N = int(input().strip())
circles = []
for _ in range(N):
    x, r = map(int, input().split())
    circles.append(CircleNode(x, r))

roots = build_tree(circles)
print(total_regions(roots))
