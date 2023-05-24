from collections import Counter

def solution(N, stages):
    nums = len(stages)
    numslist = []  # 스테이지를 클리어한 사람 수 리스트

    stages = sorted(stages)

    numslist.append(len(stages))  # 처음 스테이지는 모두 풀었으므로

    for i in Counter(stages).values():
        nums -= i  # 콜렉션으로 실패한 사람의 숫자만큼 빼어줌
        numslist.append(nums)

    numslist.pop()  # 마지막 스테이지를 클리어 한 사람을 빼줌

    dap = []  # 클리어한 사람 수 리스트
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

    fail = []  # 실패율을 저장할 리스트

    for i in range(len(numslist)):
        a = dap[i] / numslist[i]
        fail.append(a)

    sortedindex = sorted(range(N), key=lambda x: (fail[x], -x), reverse=True)

    answer = [x + 1 for x in sortedindex if x < N]

    return answer

N = 4
stages = [4,4,4,4,4]	
print(solution(N,stages))