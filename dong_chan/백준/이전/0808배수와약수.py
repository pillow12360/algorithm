# 8월 8일 다시 시작

# 배수와 약수
while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break

    if a > b:
        for i in range(1, b+1):
            if i % a and i == b:
                print("multiple")
                break
        print("neither")
    else:
        while a < b:
            num = 2
            if num * a == b:
                print("factor")
                break
            num += 1
    print("neither")

    # if a < b:
    #   for i in range(1,b+1):
    #     if i % b == 0 and i == a:
