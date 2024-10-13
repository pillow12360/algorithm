arr1 = [[1],[2]]	
arr2 = [[3],[4]]	
arr3 = []

# sum1 = []
# sum1.append(arr1[0][0]+arr2[0][0])
# sum1.append(arr1[0][1]+arr2[0][1])

# arr3.append(sum1)

# sum2 = []
# sum2.append(arr1[1][0]+arr2[1][0])
# sum2.append(arr1[1][1]+arr2[1][1])

# arr3.append(sum2)

# print(arr3)

# sum = []
# hap = []
# for i in range(len(arr1)):
#     sum = []
#     for j in range(len(arr2)):
#         sum.append(arr1[i][j] + arr2[i][j])
#     hap.append(sum)
       
  
# print(hap)

def solution(arr1, arr2):
    answer = []
    sum = []

    for i in range(len(arr1)):
        sum = []
        for j in range(len(arr2[i])):
            sum.append(arr1[i][j] + arr2[i][j])
        answer.append(sum)
    
    return answer

print(solution(arr1,arr2))