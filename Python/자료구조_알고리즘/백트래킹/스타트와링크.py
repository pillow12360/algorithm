# 10월 30일 수

# n 짝수
# 팀의 능력치 = 모든 Sij의 합
# 스타트와 링크팀의 차이를 최소화

n = int(input())
visited = [[False for _ in range(n)] for _ in range(n)]
S = []

for i in range(n):
    a = list(map(int,input().split(" ")))
    S.append(a)

# 스타트팀 i,j 링크 팀 i,j 구해야 함
def backtrack(si,sj, li,lj, cha):
    cha = min(abs((S[si][sj] + S[sj][si]) - (S[li][lj]+S[lj][li])), cha)

    for i in range(n-1):
        si,sj = i, i+1
        for j in range(n-1):
            li, lj = j, j+1

            backtrack(si,sj,li,lj,cha)

    return print(cha)

backtrack(0,1,0,1,1000)


