def backtrack(nums, remain):
    global max_value, visited

    # 숫자 상태를 문자열로 저장하여 중복 탐색 방지
    state = (tuple(nums), remain)
    if state in visited:
        return
    visited.add(state)

    # 종료 조건: 남은 교환 횟수가 0일 때
    if remain == 0:
        max_value = max(max_value, int(''.join(nums)))  # 최댓값 갱신
        return

    # 가능한 모든 교환 수행
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            # 숫자 교환
            nums[i], nums[j] = nums[j], nums[i]
            backtrack(nums, remain - 1)  # 재귀 호출
            nums[i], nums[j] = nums[j], nums[i]  # 교환 복원 (백트래킹)


T = int(input())  # 테스트 케이스 수

for t in range(1, T + 1):
    # 입력 처리
    num, k = input().split()
    nums = list(num)  # 숫자판을 리스트로 변환
    k = int(k)

    # 초기화
    max_value = 0
    visited = set()  # 중복 상태 탐색 방지용

    # 백트래킹 수행
    backtrack(nums, k)

    # 출력
    print(f"#{t} {max_value}")


'''
def backtrack( 현재상태, 선택):
    if 종료조건(현재상태):
        결과 저장
        return 
    for 선택 in 선택들:
        if 유망하지 않은 선택: #가지치기 조건
            continue
        현재상태에 선택 적용
        backtrack( 갱신된 현상, 가능한 선택):
        선택 되돌리기     
'''
