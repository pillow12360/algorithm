# n : 문서의 개수
# m : 몇번째로 출력되는 지 궁금한 문서 인덱스 번호

# 첫번째 제출

from collections import deque

t = int(input())
# 테스트 개수

for _ in range(t):

    n, m = map(int, input().split())
    # 중요도 1~9 이하의 정수
    # 중요도 중복 가능
    a = list(map(int, input().split()))

    for i in range(n):
        if i == m:
            temp = a[i]
            a[i] = (temp, 1)
        else:
            temp = a[i]
            a[i] = (temp, 0)

    d = deque(a)

    cnt = 1
    dap = {}

    while d:
        if d[0] == max(d, key=lambda x: x[0]):
            dap[cnt] = d.popleft()

            if dap[cnt][1] == 1:
                print(len(dap))
                break
            cnt += 1
        else:
            d.rotate(-1)

# 키워드
# 덱 사용
# 튜플로 해당 문서 체크
# 해당 문서일 경우 답 리스트의 길이 = 순서

# 딕셔너리의 키값으로 출력하기 위해 딕셔너리로 하였지만 리스트로도 가능 할 듯


# 두번째 제출


t = int(input())
# 테스트 개수

for _ in range(t):

    n, m = map(int, input().split())
    # 중요도 1~9 이하의 정수
    # 중요도 중복 가능
    a = list(map(int, input().split()))

    for i in range(n):
        if i == m:
            temp = a[i]
            a[i] = (temp, 1)
        else:
            temp = a[i]
            a[i] = (temp, 0)
            # 추적할 문서 체크

    d = deque(a)

    cnt = 1
    dap = []

    while d:
        if d[0] == max(d, key=lambda x: x[0]):
            dap.append(d.popleft())

            if dap[cnt-1][1] == 1:
                print(len(dap))
                break

            cnt += 1
        else:
            d.rotate(-1)

# 다른 사람의 풀이

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    queue = deque(map(int, input().split()))
    queue = deque([(i, idx) for idx, i in enumerate(queue)])
    # 각 인덱스 값을 포함한 튜플을 이용하여 체크하는 방식이 다름

    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == M:
                print(count)
                # 그저 카운터 값을 출력하는 것도 방법
                break
            else:
                queue.popleft()
        else:
            # 덱의 메서드 로테이트를 사용하지 않고 append와 popleft 의 조합으로 rotate() 구현
            queue.append(queue.popleft())
