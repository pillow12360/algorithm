n = int(input())
a = list(map(int, input().split()))

# dp 테이블을 채우는 로직은 매우 간단
for i in range(1, n):
    a[i] = max(a[i], a[i-1]+a[i])

print(max(a))  # 이 부분이 다른 문제와 다른 점
