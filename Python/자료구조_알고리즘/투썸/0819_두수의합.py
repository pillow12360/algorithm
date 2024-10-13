# 8월 19일 토요일

# 첫번째 문제 두수의 합 실버3

# twoSum 알고리즘

# N = int(input())

# nums = list(map(int, input().split()))

# target = int(input())

# 1. 리스트를 오름차순으로 정렬한다.
# 2. 포인터를 첫번째와 끝으로 설정한다.
# 3. 포인터가 타겟보다 크면 첫번째 포인터를 오론쪽으로 이동 작으면 끝 포인터를 한칸 왼쪽으로 이동
# 만약 두 포인터가 만난다면 false 반환
#  만약 target을 찾으면 True 반환

# def twoSum(nums, target):
#     nums.sort()
#     n = len(nums)

#     l, r = 0, n-1

#     while l < r:
#         if nums[l]+nums[r] > target:
#             r -= 1
#         elif nums[l]+nums[r] < target:
#             l += 1
#         elif nums[l]+nums[r] == target:
#             return True
#     return False


# print(twoSum(nums=[2, 1, 5, 7], target=4))

N = int(input())

nums = list(map(int, input().split()))

target = int(input())

nums.sort()

l, r = 0, N-1

answer = 0

while l < r:
    if nums[l] + nums[r] > target:
        r -= 1
    elif nums[l] + nums[r] < target:
        l += 1
    elif nums[l] + nums[r] == target:
        answer += 1
        l += 1
        r -= 1

print(answer)
