# 10월 24일 화요일

'''
큐는 시간 순대로 FIFO 식으로 입출력이 이루어짐

우선순위 큐는 우선순위가 높은 것부터 출력이 이루어짐

예를 들어 

7, 1, 3, 5, 6 이 우선순위큐에 차례대로 입력될 경우

숫자가 높은 경우가 우선순위가 높다면

7, 6, 5, 3, 1 순으로 dequeue가 이루어진다.

'''

import heapq

min_heap = [1,6,4,4,2,7,-5]

heapq.heapify(min_heap)
print(heapq.heappop(min_heap))

