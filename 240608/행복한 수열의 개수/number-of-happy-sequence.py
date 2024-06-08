import sys
from collections import Counter
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 예외 처리 (m=1일 때 코드에서 검사를 안함)
if m == 1 :
    print(2*n)
else:
    answer = 0
    # row에 대해 검사
    for i in range(n):
        tmp = 1  # 연속된 수열, 1 부터 시작
        for j in range(1, n):
            # 이전 값이랑 같으면 tmp += 1
            if graph[i][j-1] == graph[i][j]:
                tmp += 1

                # tmp가 m 이상이면 answer += 1 하고 해당 행 더 이상 안 봄
                if tmp >= m :
                    answer += 1
                    break
            
            else:
                tmp = 1
    # col에 대해 검사
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