M = int(input())

N = 1

while N <= M:
    N = str(N)
    hap = 0
    for i in N:
        hap += int(i)

    if (hap+int(N)) == M:
        print(N)
        break
    elif (hap+int(N)) > M:
        print(0)
        break
    else:
        N = int(N) + 1

# 실패

n = int(input())  # 분해합을 입력값으로 받음

for i in range(1, n+1):   # 해당 분해합의 생성자 찾기
    num = sum((map(int, str(i))))  # i의 각 자릿수를 더함
    num_sum = i + num  # 분해합 = 생성자 + 각 자릿수의 합
    # i가 작은 수부터 차례로 들어가므로 처음으로 분해합과 입력값이 같을때가 가장 작은 생성자를 가짐
    if num_sum == n:
        print(i)
        break
    if i == n:  # 생성자 i와 입력값이 같다는 것은 생성자가 없다는 뜻
        print(0)
