def findmin(x, y, w, h):
    left = x
    right = w - x
    up = h - y
    down = y
    return min(left, right, up, down)

arr = input().split()
x, y, w, h = int(arr[0]), int(arr[1]), int(arr[2]), int(arr[3])
print(findmin(x,y,w,h))