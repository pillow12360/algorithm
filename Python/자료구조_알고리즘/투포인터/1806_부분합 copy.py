n, s = map(int, input().split())

m = list(map(int, input().split()))

# 정확한 k 만족하는 연속하는 부분수열 누적합 구하기

# def shortest_subarray_with_sum_k(arr, k): 
#     min_length = float('inf')
#     prefix_sum = 0
#     # {누적합: 첫 번째 등장 인덱스}
#     sum_index = {0: -1}  # 처음부터의 부분배열을 위해 0을 -1로 초기화
    
#     for i, num in enumerate(arr):
#         prefix_sum += num
        
#         # prefix_sum - k가 이전에 나타났다면
#         target = prefix_sum - k
#         if target in sum_index:
#             # 부분배열 길이 = 현재 인덱스 - 시작 인덱스
#             length = i - sum_index[target]
#             min_length = min(min_length, length)
        
#         # 현재 누적합이 처음 나타나는 경우만 기록 (가장 짧은 길이를 위해)
#         if prefix_sum not in sum_index:
#             sum_index[prefix_sum] = i
    
#     return min_length if min_length != float('inf') else 0

# k이상 만족하는 모든 부분 수열의 누적합 중 가장 작은 길이를 구하는 함수
# 슬라이딩 윈도우의 크기를 줄이는 방법
def shortest_subarray_sum_at_least_s(n, s, arr):
    cur = 0
    left = 0
    answer = float('inf')
    
    for right in range(n): # 오른쪽 인덱스
        cur += arr[right]

        while cur >= s: # 타겟 숫자보다 현재 윈도우 누적합이 크면
            answer = min(answer, right - left + 1) #길이를 구해야 하므로 + 1
            
            cur -= arr[left]
            # 왼쪽 윈도우 줄이기
            left += 1

    if answer == float('inf'):
        answer = 0

    return answer
    

print(shortest_subarray_sum_at_least_s(n,s,m))