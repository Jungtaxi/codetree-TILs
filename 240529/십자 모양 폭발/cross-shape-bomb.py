import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
x, y = map(int, input().split())
x, y = x-1, y-1

bomb = graph[x][y]
bomb -= 1

def apply_grevity():
    # 각 열에 대해 아래부터 검사, 비었다면 위의 블럭과 맞바꿉니다.
    for i in range(n):
        for j in range(n-1):
            if not graph[n-j-1][i]:
                graph[n-j-1][i], graph[n-j-2][i] = graph[n-j-2][i], graph[n-j-1][i]

def remove_by_bomb():
    col_start = 0 if y - bomb < 0 else y - bomb
    col_end = n-1 if y + bomb >= n else y + bomb
    row_start = 0 if x - bomb < 0 else x - bomb
    row_end = n-1 if x + bomb >= n else x + bomb

    for i in range(col_start, col_end+1):
        graph[x][i] = 0
    for i in range(row_start, row_end+1):
        graph[i][y] = 0
    

remove_by_bomb()
apply_grevity()

for i in range(n):
    print(' '.join(map(str, graph[i])))