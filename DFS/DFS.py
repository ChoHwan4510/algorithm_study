#DFS : Depth-fisrt search(깊이 우선 탐색)
'''
  3 2
6 4 5 1
일떄 1 vertex에서 탐색을 시작한다고 가정할떄
1 2 3 4 6 5
순으로 탐색 된다
''' 

#재귀함수 : 자기자신을 호출하는 함수 주로 백트래킹,DFS에서 사용

#아이디어
"""
시작점에 연결된 Vertex 찾기
연결된 Vertex를 계속해서 찾음
더이상 연결된 Vertex 없을경우 다음
"""

#시간복잡도
#DFS : O(V+E)

#자료구조
#검색할 그래프 : 2차원배열
#방문여부 확인 : 2차원배열
#별도의 자료구조를 사용하지않고 재귀함수를 사용

#백준 2667그림 문제
#https://www.acmicpc.net/problem/2667
#아이디어
"""
- DFS로 탐색
- 2중for문, 조건은 방문을 하지 않은것(값이 1) 
- DFS를 통해 값을 저장 후 정렬
"""

#자료구조
"""
- 그래프 전체 지도 : int[][]
- 방문여부 :  boolen[][]
- 결과값 : int[]
"""

import sys
input = sys.stdin.readline

N = int(input())
map = [list(map(int,input().strip())) for _ in range(N)]
chk = [[False]*N for _ in range(N)]
result = []
each = 0

dy = [0,1,0,-1]
dx = [1,0,-1,0]
def dfs(y,x):
    global each
    each += 1 #연속된 그림의 크기 1씩증가
    for k in range(4):
        ny = y + dy[k] #상하좌우 이동
        nx = x + dx[k]
        if 0<=ny<N and 0<=nx<N : #입력받은 값까지 크기제한
            if map[ny][nx] == 1 and chk[ny][nx] == False: #방문체크
                chk[ny][nx] = True
                dfs(ny,nx) #재귀함수 호출
    

for j in range(N):
    for i in range(N):
        if map[j][i] == 1 and chk[j][i] == False:
            # 방문 체크 표시
            # DFS로 크기 구하기
            # 크기를 결과리스트에 너어주기
            chk[j][i] = True
            each = 0 #새로운 노트 탐색할때마다 0으로 초기화
            dfs(j,i) #dfs 실행
            result.append(each) #결과값 result 배열에 저장
            
result.sort()
print(len(result))
for i in result:
    print(i)


