def solution(arr):
    answer = []
    Min = min(arr)
    for i in arr:
        if i == Min:
           arr.remove(i)
    if len(arr) == 0:
        answer.append(-1)
        return answer
  
    answer = arr 
    return answer

arr = [10]

print(solution(arr))

