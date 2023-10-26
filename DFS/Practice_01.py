import sys
input = sys.stdin.readline

n,m = map(int,input().split())
map = [list(map(int,input().strip())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]
cnt = 0
each = 0
result = []
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y,x):
    global each
    each += 1 #연속된 그림의 크기 1씩증가
    for k in range(4):
        ny = y + dy[k] #상하좌우 이동
        nx = x + dx[k]
        if 0<=ny<n and 0<=nx<m : #입력받은 값까지 크기제한
            if map[ny][nx] == 1 and chk[ny][nx] == False: #방문체크
                chk[ny][nx] = True
                dfs(ny,nx) #재귀함수 호출

for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            each = 0 #새로운 노트 탐색할때마다 0으로 초기화
            dfs(j,i) #dfs 실행
            result.append(each) #결과값 result 배열에 저장
        
print(len(result))

