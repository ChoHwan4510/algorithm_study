#BFS(Breadth-fisrt search) 너비 우선 탐색

#기준 vertex에서 주위 vertex탐색을 시작하는것
'''
  3 2
6 4 5 1
일떄 1 vertex에서 탐색을 시작한다고 가정할떄
1 2 5 3 4 6
순으로 탐색 된다
''' 

#아이디어
#시작점에 연결된 Vertex 찾기
#찾은 Vertex를 Queue에 저장
#Queue의 가장 먼저 것 뽑아서 반복

#시간복잡도
#BFS : O(V+E)

#자료구조
#검색할 그래프
# 방문여부 확인(재방문 금지)
#Queue: BFS실행

#백준 1926그림 문제
#https://www.acmicpc.net/problem/1926

#아이디어
"""
- BFS로 탐색
- 2중for문, 조건은 방문을 하지 않은것(값이 1) 
- BFS로 돌면서 그림 개수+1, 최대값을 계산
"""

#시간복잡도
"""
BFS : O(V+E)
- E : 500 * 500
- V : 4 * 500 * 500
- V+E : 5 * 250000 = 100만
"""

#자료구조
"""
- 그래프 전체 지도 : int[][]
- 방문여부 :  boolen[][]
- Queue(BFS)
"""

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]
count = 0
maxv = 0

dy = [0,1,0,-1] 
dx = [1,0,-1,0]
def bfs(y,x):
    result = 1
    q = [(y,x)]
    while q: #Queue자료에 값이없을때까지 반복
        ey, ex = q.pop()
        for k in range(4):
            #상하좌우로 1칸씩 이동
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m: 
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    result += 1 # 값이 1이 있다면 그림의 크기 1씩 증가
                    chk[ny][nx] = True #상하좌우 방문 조건 True 처리
                    q.append((ny,nx)) #상하좌우 이동 처리
    return result

for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False: #입력된 그림확인 = map[j][i] / 재방문 확인 chk[j][i]
            #전체 그림 갯수 +1
            #방문 처리 True로 변경
            #BFS를 통해 그림의 크기를 구함
            #BFS 결과를 최대값에 갱신
            chk[j][i] = True
            count += 1
            maxv = max(maxv,bfs(j,i))
            
print(count)
print(maxv)
            
            
            




