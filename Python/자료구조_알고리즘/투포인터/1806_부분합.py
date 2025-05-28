n, s = map(int, input().split())

m = list(map(int, input().split()))

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

def shortest_subarray_sum_at_least_s(n, s, arr):
    """
    투 포인터를 사용하여 부분합이 S 이상인 가장 짧은 수열의 길이를 구함
    
    Args:
        n: 배열의 길이
        s: 목표 합 (이상)
        arr: 입력 배열
    
    Returns:
        int: 가장 짧은 수열의 길이 (불가능하면 0)
    """
    left = 0  # 왼쪽 포인터
    current_sum = 0  # 현재 윈도우의 합
    min_length = float('inf')  # 최소 길이
    
    # 오른쪽 포인터로 윈도우 확장
    for right in range(n):
        current_sum += arr[right]
        
        # 현재 합이 S 이상이면 윈도우 축소 시도
        while current_sum >= s:
            # 현재 윈도우 길이 업데이트
            min_length = min(min_length, right - left + 1)
            
            # 왼쪽 포인터를 오른쪽으로 이동하여 윈도우 축소
            current_sum -= arr[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0

print(shortest_subarray_sum_at_least_s(n,s,m))