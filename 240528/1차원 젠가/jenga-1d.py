import sys
input = sys.stdin.readline

def gravity_temp(n):
    tmp = [0] * n
    j = 0
    
    cnt = 0

    # O(N) 
    for i in range(n):
        if arr[i]:
            cnt += 1
            tmp[j] = arr[i]
            j += 1
 
    return tmp, cnt

n = int(input())

# 앞순이 더 높은 위치이다.
arr = []
for _ in range(n):
    arr.append(int(input()))

for _ in range(2):
    s, e = map(int, input().split())
    for i in range(s-1, e):
        arr[i] = 0
    arr, cnt = gravity_temp(n)


if arr[0] == 0:
    print(0)
else:
    print(cnt)
    for i in range(n):
        if arr[i] :
            print(arr[i])