T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    N, P = map(int, input().split())  # 선택 횟수와 폭탄 층 입력

    # N번 선택의 최대 합
    max_floor = N * (N + 1) // 2

    # 폭탄 층을 확인하며 조정
    current_sum = 0
    for i in range(1, N + 1):
        current_sum += i
        if current_sum == P:
            max_floor -= 1
            break

    print(max_floor)