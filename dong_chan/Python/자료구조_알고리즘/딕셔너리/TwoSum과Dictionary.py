# 딕셔너리를 이용하여 더욱 효율적인 알고리즘 설계

# 딕셔너리의 key 에 nums의 요소를 입력
# nums for을 돌며 딕셔너리에 필요한 숫자가 있는지 in 으로 확인

# 딕셔너리의 in 연산자로 바로 필요한 요소의 유무를 확인

# hash function

# 메모리를 사용하여 시간복잡도를 낮추는 방법

# 코드 설계

nums = [4, 1, 9, 7, 3, 16]
target = 14


def dicTwoSum(nums, target):
    dic = {}
    for i in nums:
        dic[i] = True

    for i in nums:
        n = target - i
        if n in dic and i != n:
            return True
    return False

# 이 함수는 같은 원소를 두번 찾게 되는 문제가 있다. 그 문제를 수정하라 => 수정 완료


print(dicTwoSum(nums, target))
