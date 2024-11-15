# x += y 또는 y += x
# 원하는 만큼 수행

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b, n = map(int,input().split())

    cnt = 0

    while True:
        
        if a < b:
          a+=b
          cnt += 1

        elif b < a:
          b+=a
          cnt += 1
        
        elif b == a:
          a+=b
          cnt += 1

        if a > n or b > n:
          break

    print(cnt)
