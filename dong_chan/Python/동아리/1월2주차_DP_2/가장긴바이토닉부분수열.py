# 1월 14일 일요일

# dp 골드4

# 가장 긴 바이토닉 부분 수열을 찾는 문제
# 길이 출력


# 1월 15일 정답 확인
# https://seohyun0120.tistory.com/entry/%EB%B0%B1%EC%A4%80-11054-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EB%B0%94%EC%9D%B4%ED%86%A0%EB%8B%89-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-%ED%92%80%EC%9D%B4

# LIS -> 가장 긴 증가하는 부분 수열의 변형 문제
# https://seohyun0120.tistory.com/entry/%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4LIS-%EC%99%84%EC%A0%84-%EC%A0%95%EB%B3%B5-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC

x = int(input())

case = list(map(int, input().split()))

reverse_case = case[::-1]
# [::-1]은 시작 인덱스와 끝 인덱스를 생략하고, 스텝(step)을 -1로 설정. 이는 리스트의 마지막 요소부터 시작하여 역순으로 모든 요소를 포함

increase = [1 for _ in range(x)]  # 가장 긴 증가하는 부분 수열
decrease = [1 for _ in range(x)]  # 가장 긴 감소하는 부분 수열(reversed)

for i in range(x):
    for j in range(i):
        if case[i] > case[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if reverse_case[i] > reverse_case[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

# 가장 긴 증가, 감소 하는 부분 수열을 각각 구한 뒤

result = [0 for _ in range(x)]

for i in range(x):
    result[i] = increase[i] + decrease[x-i-1] - 1

# 인덱스 마다 가장 긴 증가하는 부분 수열과 감소하는 부분 수열을 더한 후 리스트에 저장
# 가장 큰 수가 중복되기 때문에 -1

print(max(result))
# 그중 가장 긴 것을 출력
