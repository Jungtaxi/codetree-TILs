import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
x, y = map(int, input().split())
x, y = x-1, y-1

bomb = graph[x][y]
bomb -= 1

def apply_gravity():
    # 각 열에 대해 아래부터 검사, 비었다면 위의 블럭과 맞바꿉니다.
    for i in range(n):
        for j in range(n-1):
            if not graph[n-j-1][i]:
                graph[n-j-1][i], graph[n-j-2][i] = graph[n-j-2][i], graph[n-j-1][i]

def remove_by_bomb():
    for i in range(-bomb, bomb + 1):
        # col 방향
        if x + i >= 0 and x + i < n :
            graph[x + i][y] = 0
        # row 방향
        if y + i >= 0 and y + i < n :
            graph[x][y + i] = 0
    

remove_by_bomb()
apply_gravity()

for i in range(n):
    print(' '.join(map(str, graph[i])))