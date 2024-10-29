'''
10월 28일 월

문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

'''
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

n, m = map(int,input().split())

num_list = []


def backtrack(num_list, m):
    # 현재 수열의 길이가 m이면 출력하고 종료
    if len(num_list) == m:
        print(" ".join(map(str, num_list)))  # 공백으로 구분하여 출력
        return

    # 1부터 n까지의 숫자를 탐색
    for i in range(1, n + 1):
        if i not in num_list:  # 중복을 방지
            num_list.append(i)  # 숫자를 추가
            backtrack(num_list, m)  # 재귀적으로 다음 숫자를 선택
            num_list.pop()  # 백트래킹: 선택한 숫자를 제거하고 돌아가기

backtrack(num_list, m)


