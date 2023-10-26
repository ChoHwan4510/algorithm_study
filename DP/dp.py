#DP(Dynamic Programming)
#이전의 값을 재활용 하는 알고리즘
#예시 :1~10 숫자 중, 각각 이전값들을 합한 값 구하기
#이전의 값을 활용해서 시간복잡도 줄일 수 있음
#점화식이 필요하다 EX) An = An-1+An-2

#백준
#https://www.acmicpc.net/problem/11726

#아이디어
"""
- 점화식 : An = An-1 + An-2
- N값을 구하기 위해, for문 3부터 N까지의 값을 구해주기
- 이전값, 이전이전값을 더해서 10007로 나누어 저장
"""

#시간복잡도
# O(N)

#자료구조
# -DP 값 저장하는 (경우의수) 배열 : int[]

import sys
input = sys.stdin.readline

n = int(input())
rs = [0,1,2]

for i in range(3, n+1):
    rs.append((rs[i-1] + rs[i-2])%10007)
    
print(rs[n])
    
