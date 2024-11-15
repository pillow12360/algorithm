from collections import deque

N, K = map(int, input().split())

arr = list(map(int, input().split(' ')))

# print(arr)

arr = deque(arr)

arr.rotate(K)

for i in arr:
    print(i, end=" ")