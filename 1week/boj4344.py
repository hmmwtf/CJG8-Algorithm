ca  = int(input())

for i in range(ca):
    arr = input().split()
    #학생 수
    stunum = int(arr[0])

    #문자열 배열 정수 변환
    for j in range(1, stunum+1):
        arr[j] = int(arr[j])
    
    total = 0
    for k in range(1, stunum+1):
        total += arr[k]
    avg = total/stunum
    
    result = 0
    for l in range(1, stunum+1):
        if arr[l] > avg:
            result += 1
    print(f"{(result/stunum)*100:.3f}%")
