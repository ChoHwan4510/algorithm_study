#투포인터
#각 원소마다 모든값을 순회해야할때,O(N^2)
#연속하다는 특성을 이용해서 처리, O(N)
#두개의 포인터(커서)가 움식이면서 계산
#처음부터 생각하기가 어렵다, 쉬운방법부터 생각하자

#백준 2559 수열
#https://www.acmicpc.net/problem/2559

#아이디어
#처음에 K개의 값을 구함
#for문 : 다음 인덱스의 값을 더하고, 앞 인덱스의 값을 빼준다 이때 최대값을 갱신
#

#시간복잡도
#숫자 개수만큼 fro => O(N)

#자료구조
#전체 정수 배열 : int[]
#수 모두 -100~100 > int 가능
#합한 수 : int
# 100*1e5 = 1e7 > int 가능

import sys
input = sys.stdin.readline

N,K = map(int,input().split())
nums = list(map(int,input().split()))
each = 0

#k개를 더해주기
for i in range(K):
    each += nums[i]
maxv = each

#다음인덱스를 더해주고, 이전인덱스를 빼주기
for i in range(K,N):
    each += nums[i]
    each -= nums[i-K]
    maxv = max(maxv, each)

print(maxv)

#팁
"""
처음부터 생각하기 어려움, 쉬운방법부터 생각
for 내부 투포인터 계산하는 값의 최대값 확인 필수(INT범위 초과)
투포인터 문제 종류
- 두개 다 왼쪽에서 /각각 왼쪽, 오른쪽/다른 배열
- 일반 O(N) / 정렬 후 투포인터 : O(NigN)
"""
    
    
    



