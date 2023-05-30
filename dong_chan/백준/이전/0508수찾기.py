def binary_search (target, data):

  start = 0
  end = len(data) - 1

  while start <= end:
    mid = (start + end) // 2
    if data[mid] == target:
      return mid
    elif data[mid] < target:
      start = mid + 1
    elif data[mid] > target:
      end = mid - 1
    else:
      end = mid - 1
  return None

num1 = input()
Array1 = map(int,input().split())

num2 = input()
Array2 = input().split()

for i in Array2:
    target = int(i)
    if binary_search(target, Array1) is None:
      print(0)
    else:
      print(1)