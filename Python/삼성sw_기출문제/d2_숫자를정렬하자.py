T = int(input())

for t in range(1,T+1):

    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()

    answer = ""

    for i in nums:
        i = str(i)
        answer += i
        answer += " "

    answer.strip()

    print(f'#{t} {answer}')