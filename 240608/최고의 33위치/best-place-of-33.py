import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n-2):
    for j in range(n-2):
        tmp = 0
        for k in range(3):
            for l in range(3):
                tmp += graph[i+k][j+l]
        if tmp > ans :
            ans = tmp

print(ans)