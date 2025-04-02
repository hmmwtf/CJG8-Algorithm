import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline 

tree = []
while True:
    try:
        tree.append(int(input().strip()))
    except:
        break

def postorder(start, end):
    if start > end:
        return
    
    right_subtree_start = end + 1
    for i in range(start + 1, end + 1):
        if tree[i] > tree[start]:
            right_subtree_start = i
            break
        
    postorder(start + 1, end - 1)
    postorder(right_subtree_start, end)
    
    print(postorder[start])

postorder(0, len(tree)-1)