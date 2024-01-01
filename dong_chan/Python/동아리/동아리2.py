def find_longest_common_substring(str1, str2):

    m = len(str1)
    n = len(str2)

    # LCSuff는 공통 부분의 길이를 저장하는 테이블
    lcsuff = [[0] * (n + 1) for _ in range(m + 1)]
    result = 0  # 최대 공통 부분의 길이
    end_index = 0  # 최대 공통 부분의 끝 인덱스

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcsuff[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                lcsuff[i][j] = lcsuff[i - 1][j - 1] + 1
                if lcsuff[i][j] > result:
                    result = lcsuff[i][j]
                    end_index = i - 1
            else:
                lcsuff[i][j] = 0

    # 최대 공통 부분을 찾아서 출력
    common_substring = str1[end_index - result + 1: end_index + 1]
    return common_substring

# 두 대의 자동차 문자열 입력
car1 = "ABCDG"
car2 = "AFDFSDFDFSDFSDFACDGFDSFDSFDFSF"

# 최장 공통 부분 문자열 찾기
common_substring = find_longest_common_substring(car1, car2)

print("최대 공통 부분 문자열:", common_substring)