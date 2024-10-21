from bisect import bisect_left


# LIS를 구하는 함수
def lis(sequence):
    lis_sequence = []  # LIS를 저장할 리스트

    for num in sequence:
        # LIS에서 num이 들어갈 위치를 찾는다 (이진 탐색 활용)
        pos = bisect_left(lis_sequence, num)

        if pos < len(lis_sequence):
            # 만약 해당 위치가 이미 존재하면 값을 교체한다
            lis_sequence[pos] = num
        else:
            # 해당 위치가 LIS의 길이와 같다면 새로 값을 추가한다
            lis_sequence.append(num)

    return len(lis_sequence)  # LIS의 길이를 반환


# 전깃줄 문제 해결 함수
def min_remove_wires(n, wires):
    # 전봇대 A의 위치를 기준으로 정렬
    wires.sort(key=lambda x: x[0])

    # 전봇대 B의 위치로 이루어진 수열 추출
    b_positions = [wire[1] for wire in wires]

    # 최대 증가 부분 수열의 길이 구하기
    max_non_crossing_wires = lis(b_positions)

    # 제거해야 하는 최소 전깃줄의 개수
    return n - max_non_crossing_wires


# 입력 처리
n = int(input())  # 전깃줄의 개수
wires = [tuple(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(min_remove_wires(n, wires))