import sys
from collections import Counter
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

answer = 0
for i in range(n):
    tmp = 1
    for j in range(1, n):
        if graph[i][j-1] == graph[i][j]:
            tmp += 1

            if tmp >= m :
                answer += 1
                break
        
        else:
            tmp = 1

for i in range(n):
    tmp = 1
    for j in range(1, n):
        if graph[j-1][i] == graph[j][i]:
            tmp += 1

            if tmp >= m :
                answer += 1
                break
        
        else:
            tmp = 1

print(answer)