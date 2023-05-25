from collections import Counter

def solution(N, stages):
   answer = []

   N = 5
   stages = [2, 1, 2, 6, 2, 4, 3, 3]

   stages= sorted(stages)

   nums = len(stages)
   numslist = [] # 스테이지를 클리어한 사람 수 리스트

   numslist.append(len(stages)) # 처음 스테이지는 모두 풀었으므로

   for i in Counter(stages).values():
      nums -= i # 콜렉션으로 실패한 사람의 숫자만큼 빼어줌 
      numslist.append(nums)

   numslist.pop() # 마지막 스테이지를 클리어 한 사람을 빼줌

   dap = [] # 클리어한 사람 수 리스트
   counter = Counter(stages)
   set1 = sorted(set(stages))

   # 마지막 스테이지를 클리어한 예외 발생 처리

   removecount = 0 
   for i in set1:
      if N < i:
         set1.remove(i)
         removecount += 1

   for i in set1:
      dap.append(counter[i])

   for i in range(removecount):
      dap.append(0)


   fail = [] # 실패율을 저장할 리스트 

   for i in range(len(numslist)):
      a = 0
      a = dap[i] / numslist[i]
      fail.append(a)


   daplist = list(range(1,N+1))

   # sortedindex = sorted(range(len(fail),), key=lambda x:(fail[x],daplist[x]),reverse=True)

   # 아래 코드는 람다식을 활용하였음 gpt의 도움을 받음 
   sortedindex = sorted(range(len(fail)), key=lambda x: (fail[x], -x - 1), reverse=True)


   answer = [x + 1 for x in sortedindex]


   return answer



N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N,stages))



# stages= sorted(stages)



# # print(sorted(Counter(stages)))

# # print(solution(N,stages))

# nums = len(stages)
# numslist = [] # 스테이지를 클리어한 사람 수 리스트

# numslist.append(len(stages)) # 처음 스테이지는 모두 풀었으므로

# for i in Counter(stages).values():
#    nums -= i # 콜렉션으로 실패한 사람의 숫자만큼 빼어줌 
#    numslist.append(nums)

# numslist.pop() # 마지막 스테이지를 클리어 한 사람을 빼줌

# # dap = []
# # count = 0
# # for i in Counter(stages).values():
# #     count +=1
# #     if not count == N:
# #       dap.append(i)
# #     else:
# #        dap.append(0)

# dap = [] # 클리어한 사람 수 리스트
# counter = Counter(stages)
# set1 = sorted(set(stages))

# # 마지막 스테이지를 클리어한 예외 발생 처리

# removecount = 0 
# for i in set1:
#   if N < i:
#     set1.remove(i)
#     removecount += 1

# for i in set1:
#     dap.append(counter[i])

# for i in range(removecount):
#    dap.append(0)


# fail = [] # 실패율을 저장할 리스트 

# for i in range(len(numslist)):
#    a = 0
#    a = dap[i] / numslist[i]
#    fail.append(a)


# daplist = list(range(1,N+1))

# sortedindex = sorted(range(len(fail),), key=lambda x: (fail[x],daplist[x]),reverse=True)

# sortedfail = [daplist[i] for i in sortedindex]

# answer = sortedfail

# print(answer)
