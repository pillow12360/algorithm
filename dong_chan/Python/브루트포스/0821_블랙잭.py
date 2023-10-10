# 08월 21일 브론즈2 블랙잭

from itertools import combinations, permutations

N, M = map(int, input().split())

nums = list(map(int, input().split()))

perm = list(combinations(nums, 3))

hap = []

for i in perm:
    if i[0]+i[1]+i[2] <= M:
        hap.append(i[0]+i[1]+i[2])

print(max(hap))
