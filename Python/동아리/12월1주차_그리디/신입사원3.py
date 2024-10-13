T = int(input())  # 테스트 개수 T(1 ≤ T ≤ 20)
# 지원자의 숫자 N(1 ≤ N ≤ 100,000)

for _ in range(T):
    cnt = 0
    N = int(input())
    saram = []
    for _ in range(N):
        saram.append(list(map(int, input().split())))  # 등수

    saram = sorted(saram)

    top = 0
    result = 1

    for i in range(1, len(saram)):
        if saram[i][1] < saram[top][1]:
            top = i
            result += 1
    print(result)
