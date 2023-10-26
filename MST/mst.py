#MST(Minimum Spanning Tree)
#Spanning Tree : 모든 노드가 연결된 트리
#MST :최소의 비용으로 모든 노드가 연결된 트리

#MST 푸는 방법 : Kruskal or Prim
#Kruskal : 전체 간선 중 작은것부터 연결 (Union-find 알고리즘 사용)
#Prim : 현재 연결된 트리에 이어진 간선중 가장 작은것을 추가

#heap 자료구조
#최대값, 최소값 빠르게 계산하기 위한 자료구조
#이진트리 구조
#처음 저장할때부터 최대값 or 최소값 결정하도록

#핵심코드
heap = [[0,1]]
while heap:
    w, next_node = heapq.heappop(heap)
    if chk[next_node] == False:
        chk[next_node] == True
        rs += w
    for next_edge in edge[next_node]:
        if chk[next_edge[1]] == False:
            heapq.heappush(heap,next_edge)