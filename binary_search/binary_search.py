#이진탐색(Binary search)
#어떤 값을 찾을 때 정렬의 특징을 이용해 빨리 찾음
#정렬되어있을 경우, 어떤 값 찾을때 사용: O(N) -> O(IgN)
#처음부터 생각하기 어려움, 쉬운방법부터 생각
#반을 잘라서 비교하는 방법

#예시
#1~4 숫자중 특정 숫자를 찾아야 할 때
# 모두 탐색: O(N)
# 이진 탐색: O(lgN)

#핵심코드
"""
def search(st, en, target): #시작인덱스, 끝인덱스, 타겟인텍스
    if st == en:
        # ~~
        return

    mid = (st+en) // 2 #중간 구하기
    if nums[mid] < target:
        search(mid + 1,en, target)
    else:
        search(st, mid, target)
"""
#백준 1920문제
#https://www.acmicpc.net/problem/1920

#아이디어
# - N개의 숫자를 정렬
# - M개를 for 돌면서, 이진탐색
# - 이진탐색 안에서 마지막에 데이터를 찾으면, 1출력, 아니면 0출력

#시간복잡도
# - N개 입력값 정렬 = O(NlgN)
# - M개를 N개중에서 탐색 = O(M*lgN)

#자료구조
#- N개 숫자 : int[]
#- M개 숫자 : int[]

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
M = int(input())
target_list = list(map(int,input().split()))

nums.sort() #정렬을 먼저해야 이진탐색 가능

def search(st,en,target):
    if st == en:
        if nums[st] == target:
            print(1)
        else:
            print(0)
        return
    
    mid = (st+en)//2
    if nums[mid] < target:
        search(mid+1, en, target)
    else:
        search(st, mid, target)


for each_target in target_list:
    search(0, N-1, each_target)
    
#tip
#입력의 개수가  1E5정도의 경우라면 의심