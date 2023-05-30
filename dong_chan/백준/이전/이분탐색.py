def binary_search (target, data): # nlogn
  start = 0
  end = len(data) - 1

  while start <= end:
    mid = (start + end) // 2

    if data[mid] == target:
      return mid
    elif data[mid] < target:
      start = mid + 1
    elif data[mid] > target:
      start = mid - 1
    else:
      end = mid - 1

  return None
  

A = [23,56,321,32,113,44]
target = 321
B = binary_search(target, A)

print(B)
print(A[B])