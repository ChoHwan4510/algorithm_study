#백트랙킹
#모든 경우의수를 확인해야 할때 사용함
#for문으로 확인이 불가능한 경우(깊이가 달라질때)

#백준문제
#https://www.acmicpc.net/problem/15649

#아이디어
# - 1부터 n중에 하나를 선택한 뒤 다음 1부터 N부터 선택할때 이미 선택한 값이 아닌경우 선택
#- M개를 선택한 경우 프린트

#시간복잡도
# N^N : 중복이 가능, N = 8까지 가능
# N! : 중복이 불가, N = 10까지 가능

#자료구조
#방문 여부 확인 : bool[]
#선택한 값 입력 배열 : int[]

import sys
input = sys.stdin.readline
N,M = map(int,input().split())
rs = [] #결과값
chk = [False] * (N+1) #방문여부

def recur(num):
    if num == M: #체크값이 M값과 같을때 결과 출력
        print(' '.join(map(str,rs)))
        return
    for i in range(1, N+1):
        if chk[i] == False:
            chk[i] = True
            rs.append(i)
            recur(num+1)
            
            chk[i] = False
            rs.pop()
recur(0)

#백트래킹 문제는 N이 작음
# 재귀함수 사용할때, 종료시점 잊지말기