# 08월 16일 2번째 문제

N = int(input())

list1 = list(sorted(map(int, (input().split()))))

tmp = 0

answer = 0

for i in list1:
    tmp += i
    answer += tmp

print(answer)

# 성공
