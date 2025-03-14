a = int(input())
b = int(input())
c = int(input())

n = a * b * c 
arr = [0 for i in range(10)]

while(n > 0):
    digit = n % 10
    if digit == 0:
        arr[0] += 1
    elif digit == 1:
        arr[1] += 1
    elif digit == 2:
        arr[2] += 1
    elif digit == 3:
        arr[3] += 1
    elif digit == 4:
        arr[4] += 1    
    elif digit == 5:
        arr[5] += 1
    elif digit == 6:
        arr[6] += 1
    elif digit == 7:
        arr[7] += 1
    elif digit == 8:
        arr[8] += 1
    elif digit == 9:
        arr[9] += 1
    n //=10

for k in range(10):
    print(arr[k])