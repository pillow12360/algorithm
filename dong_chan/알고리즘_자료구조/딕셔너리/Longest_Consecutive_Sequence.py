# 0821 월요일 인프런 코테

# 정렬되지 있지 않은 정수형 배열 nums 가 주어졌다. nums 원소는 가지고 만들 수 있는 가장 긴 연속된 수의 갯수는 몇개인지 반환하시오.

# 딕셔너리 자료구조로 시간 탐색의 시간복잡도를 줄이고, 반복되는 중복을 제거함으로 최대한으로 시간복잡도를 낮추는 방법을 사용해야함

# 정렬을 사용하지 않는 방법 1, 정렬 사용 방법 2

nums = [100, 4, 200, 1, 3, 2, 5]


def longestConsecutive(nums):
    longest = 0
    num_dict = {}
    # 딕셔너리의 키값은 중복되지 않으므로 중복 요소가 자동으로 제거

    # for num in nums:
    #     num_dict[num] = True
    # value 값은 사용하지 않으므로 모두 True

    # 해쉬 set을 이용하여 간결하게 표현 가능
    # num_set = set(nums) 집합 자료형도 딕셔너리와 동일하게 in 의 시간복잡도가 1 이고 사용하는 방법도 같다
    # num_dict = {x:x+1 for x in nums} 파이썬의 컴프리엔션 value를 키값의 +1설정하여 value값 까지 활용

    num_dict = {x: x+1 for x in nums}

    for num in num_dict:
        if num-1 not in num_dict:  # 조건문의 in
            cnt = 1
            target = num + 1
            while target in num_dict:  # 이 in 도 딕셔너리의 in과 같다 빅오 1
                target += 1  # 특정조건에서만 while문이 실행되므로 n제곱이 아닌 2n이 된다.
                cnt += 1
            # 기존의 longest 와 현재 구한 cnt와 비교하여 더 큰 수를 longest로 설정함
            longest = max(longest, cnt)
            # 결론적으로 가장 큰 cnt를 찾게 된다.

    return longest


print(longestConsecutive(nums))
