# 최장 공통 부분 수열(LCS) 10월6일 복습
import sys
read = sys.stdin.readline
# 입출력 시간 개선

string1, string2 = read().strip(), read().strip()

X = len(string1) + 1
Y = len(string2) + 1

dp = [[0] * Y for _ in range(X)] # dp 테이블 초기화

for y in range(1, Y):
    for x in range(1, X):
        if string1[y-1] == string2[x-1]:
            dp[y][x] = dp[y-1][x-1] + 1
        else:
            dp[y][x] = max(dp[y][x-1], dp[y-1][x])

print(dp[-1][-1])
'''
유튜브 강의를 통해 학습하였다. 

bottom - up 방식으로 2차원 dp 테이블을 채워나가는 것이 핵심이다.

여기서 처음으로 배운 것


1. 부분 문자열을 다른 표현방식으로 치환

2. dp table을 구할 때 다양한 조건식 사용

3. 2차원 dp 테이블을 활용할 것

4. 초기값 0을 dp 테이블을 선언 시 초기화 한것
'''