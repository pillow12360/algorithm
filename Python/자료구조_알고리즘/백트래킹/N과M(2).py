# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
# 10월 28일 월

n, m = map(int,input().split())

num_list = []

def backtrack(num_list, m):
    # 현재 수열의 길이가 m이면 출력하고 종료
    if len(num_list) == m:
        print(" ".join(map(str, num_list)))  # 공백으로 구분하여 출력
        return

    # 1부터 n까지의 숫자를 탐색
    for i in range(1, n + 1):
        if not num_list or (i not in num_list and num_list[-1] < i):  # 마지막 숫자보다 큰 숫자만 선택
            num_list.append(i)  # 숫자를 추가
            backtrack(num_list, m)  # 재귀적으로 다음 숫자를 선택
            num_list.pop()  # 백트래킹: 선택한 숫자를 제거하고 돌아가기

backtrack(num_list, m)