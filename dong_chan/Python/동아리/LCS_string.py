car1 = input()
car2 = input()

dp = [[0 for _ in range(len(car2) + 1)] for _ in range(len(car1) + 1)]

car1 = [0] + list(car1)
car2 = [0] + list(car2)

length = 0
end_position = 0  # 최장 공통 부분 문자열의 끝 위치

for i in range(1, len(car1)):
    for j in range(1, len(car2)):
        if car1[i] == car2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            if dp[i][j] > length:
                length = dp[i][j]
                end_position = i  # 최장 공통 부분 문자열의 끝 위치 업데이트

# 최장 공통 부분 문자열 찾기
start_position = end_position - length # 시작점은 가장 끝점 - 문자열의 길이
LCS = car1[start_position:end_position]

print(length)
print(LCS)