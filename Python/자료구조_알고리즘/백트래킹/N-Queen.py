# 10월 29일 화

n = int(input())
answer = 0

# 유효성 체크를 위한 변수들
cols = [False] * n
diag1 = [False] * (2 * n - 1)  # 대각선 1 (row + col)
diag2 = [False] * (2 * n - 1)  # 대각선 2 (row - col + n - 1)

# row 는 0부터 n 까지 증가함
def backtrack(row):
    global answer
    if row == n: # 퀸을 n개 모두 놓았다면 경우의 수 하나 증가
        answer += 1
        return

    for col in range(n):
        # 대각선 2개 와 column 열이 모두 false 일 때만 = 퀸을 놓을 수 있을 때 만 (Row는 자동적으로)
        if not cols[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
            # 퀸을 놓는다
            cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True
            # 왼쪽 아래에서 오른쪽 위로 향하는 대각선의 인덱스는 row + col
            # 오른쪽 아래에서 왼쪽 위로 향하는 대각선의 인덱스는 row - col + n - 1로 계산
            # 대각선 두개와 컬럼에 공격범위를 모두 true로 설정 후
            backtrack(row + 1) # dfs
            # 퀸을 제거한다
            cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False

backtrack(0)

print(answer)