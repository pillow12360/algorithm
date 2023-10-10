import sys

A,B,C = map(int,sys.stdin.readline().rstrip().split())

D = C-B

if C <= B:
    N = -1
else:
    N = A // D + 1

print(N)

#소요시간 약 20분
#C와 B가 같은 반례를 찾지 못하여 약 10분 더 소모

# 참고한 내용 없이 풀었음

#처음에는 while문과 if문으로 N의 값을 처음부터 구하려 하였으나 마지막의 입출력으로 힌트를 얻어 수학 식으로 더욱 간결하게 코드를 수정함


