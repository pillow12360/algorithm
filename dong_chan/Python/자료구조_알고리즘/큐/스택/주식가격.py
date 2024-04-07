from collections import deque


def solution(prices):
    answer = []
    cur_index = 0
    q = deque(prices)

    while q:
        cur_price = q.popleft()
        q2 = deque(q)
        print(q2)
        cnt = 0

        while q2:
            cnt += 1
            com_price = q2.popleft()

            if com_price >= cur_price:
                continue
            else:
                answer.append(cnt)
                break

    return answer


prices = [1, 2, 3, 2, 3]

print(solution(prices))
