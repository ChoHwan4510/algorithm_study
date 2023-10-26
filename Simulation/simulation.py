#시뮬레이션

#각 조건에 맞는 상황을 구현하는 문제
# - 지도상에서 이동하면서 탐험하는 문제
# - 배열안에서 이동하면서 탐험하는 문제

#별도의 알고리즘 없이 풀수 있으나, 구현력 중요

#백준14503
#https://www.acmicpc.net/problem/14503

#아이디어
#특정조건 만족할때까지 반복 -> while문
#4방향 탐색 먼저 수행 > 빈칸 있을경우 이동
#4방향 안될 경우, 뒤로 한칸 가서 반복
#후진이 불가능하면 종료

#시간복잡도
#while문 최대 : N x M
#각 칸에서 4방향 연산 수행
#O(NM)

#자료구조
#전체 지도: int[][] / 0청소x,  1:벽, 2:청소o
#내 위치, 방향 : int, int, int / y, x, d

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
y,x,d = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
#방향벡터
dy = [-1,0,1,0]
dx = [0,1,0,-1]

while 1:
    if map[y][x] == 0:    
        map[y][x] = 2 #해당구역 청소
        cnt += 1
    switch = False
    for i in range(1,5): #청소구역 탐색(4방향 바라보기)
        ny = y + dy[d-i] #다음방향 바라보기
        nx = x + dx[d-i]
        if 0<=ny<N and 0<=nx<M: #구역크기 체크
            if map[ny][nx] == 0: #청소하지 않은 구역일때
                #한칸 이동
                d = (d-i+4) %4
                y = ny 
                x = nx
                switch = True
                break
    #4방향 모두 있지 않은 경우
    if switch == False:
        #뒤쪽 방향이 막혀있는지 확인
        ny = y - dy[d]
        nx = x - dx[d]
        if 0<=ny<N and 0<=nx<M:
            if map[ny][nx] == 1:
                break
            else:
                #뒤로 후진
                y = ny
                x = nx
        else:
            break
print(cnt)
    
        
            
        
    






