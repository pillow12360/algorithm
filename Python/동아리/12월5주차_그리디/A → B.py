# 12월 30일 실버 2

# 그리디
'''
정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

2를 곱한다.
1을 수의 가장 오른쪽에 추가한다. 
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.
'''

# 2가지 경우의 수

# top-down 방식

# 끝자리에 1이 있다면 1을 빼는 것
# 나머지는 2로 나눌 것

from collections import deque
A, B = map(int, input().split())
count = 1

while (B != A):
    count += 1
    temp = B
    if B % 10 == 1:  # 나머지 연산자로 1의 자리가 1일 경우
        B //= 10  # 10을 몫의 나눗셈을 하여 결과적으로 1을 제거
    elif B % 2 == 0:  # 짝수일 경우
        B //= 2  # 2로 나누어줌

    if temp == B:  # 만약 2계산 모두 해당 되지 않을 경우 계산 불가
        print(-1)
        break
else:
    print(count)

# 자바스크립트와 언어적 문법 헷갈림
# 10의 // 연산으로 1의 자리 없애는 것
# 그리디 문제이지만 top-down 방식 (dp)를 이용하여 푼 것
# 그리디 문제라고 생각하고 접근하였는데 보자마자 dp스러운 문제였다.
# 그래프로도 풀 수 있는 문제라는것도 신기함

# 그래프 풀이 bottom - up

A, B = map(int, input().split())
q = deque()
q.append((A, 1))  # t는 계산 횟수를 저장함
count = 0

while (q):
    n, t = q.popleft()  # n은 계산의 대상 t는 계산 횟수

    if n > B:  # n이 만약 B보다 크면 다음을 실행하지 않고 반복
        continue
    if n == B:  # n이 만약 B와 같다면 계산 완료
        print(t)
        break
    q.append((int(str(n)+"1"), t+1))  # 2 가지의 경우의 수를 다음에 계산할 큐에 저장
    q.append((n*2, t+1))
else:
    print(-1)

# 그래프의 활용성을 다시 상기할 수 있었다.
# 계산 대상과 횟수를 튜플 자료형으로 같이 처리하는 로직
# 두가지의 경우의 수를 모두 실행해보며 탐색하는 BFS
