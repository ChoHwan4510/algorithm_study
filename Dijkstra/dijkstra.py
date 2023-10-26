#다익스트라
#한 노드에서 다른 모든 노드까지 가는데 최소비용

#작동원리
#간선: 인접리스트, 거리배열: 초기값 무한대로설정, 힙 시작점 추가
#힙에서 현재 노드를 빼면서, 간선 통할 때 더 거리 짧아진다면 거리 생신 및 힙에 추가

#핵심코드
# dist[K] =0 #거리초기값
# heapq.heappush(heap,(0,K)) #초기 heap값

# while heap:
#     w,v = heapq,heappop(heap) # w:현재 비용,  v:현재노드
#     if w != dist[v]: continue #현재비용과 거리배열에서 관리하고 있는 최신값과 일치하는지 비고
#     for nw,nv in edge[v]: #간접리스트에서 간선과 볼텍스뽑기
#         if dist[nv] > dist[v]+nw: #현재 노드가 더 크다면 갱신
#             dist[nv] = dist[v] + nw
#         heapq.heappush(heap,(dist[nv].nv))
        
#백준
#https://www.acmicpc.net/problem/1753

#아이디어
#한점에서 다른 모든 점으로의 최단경로 > 다익스트라
#모든 점 거리 초기값 무한대로 설정
#시작점 거리 0 설정 및 힙에 추가
#힙에서 하나씩 빼면서 수행할 것
#-현재거리가 새로운 간선 거칠때보다 크다면 갱신
#-새로운 거리 힙에 추가

#시간복잡도
#O(ElgV)

#변수
#다익스트라 사용 힙 : (비용(int), 다음노드(int))[]
#- 비용최대값 : int
#- 다음 노드 : 2e4 => int
#거리 배열 int[]
#- 거리 최대값 : int 가능
#간선,인접 리스트 : (비용(int),다음 노드(int))[]

import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int,input().split())
K = int(input())
edge = [ [] for _ in range(V+1)]
dist = [INF] * (V+1) #거리배열
for i in range(E):
    u,v,w = map(int,input().split()) #노드셋팅
    edge[u].append([w,v]) #간접리스트
    
#시작점 초기화
dist[K] = 0
heap = [[0,K]]

while heap:
    ew, ev= heapq.heappop(heap) #현재의무게, 현재의 노드 heap에 있는 제일 첫번째 가져오기
    if dist[ev] != ew: continue #최신값인지 확인
    for nw, nv in edge[ev]: #다음 인접리스트,무게 확인
        if dist[nv] > ew + nw: #다음 인접리스트가 더 클떄 
            dist[nv] = ew + nw
            heapq.heappush(heap, [dist[nv],nv])

for i in range(1, V+1):
    if dist[i] == INF: print("INF")
    else: print(dist[i])