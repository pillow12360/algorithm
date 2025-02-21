#11월 2일 인프런 강의

# 백트래킹 개요

# 리스트 [4, 9, 7, 5, 1] 에서 세 개의 숫자를 더해서 15이 될 수 있나요?

# 모든 후보들을 나열 - state tree

'''
완전 탐색

모든 가능성을 하나하나 살펴본다.

내가 찾는 답이 아니라면 넘어간다.

모든 후보들을 비교해 본 후 정답일 때 바로 return 하거나 전부 비교한후 반환하는 방법이 있다.

'''

# word search 예시 문제

'''
word search

알파벳이 저장된 그리드가 주어진 후 해당되는 단어가 있는지 찾는 것

하지만 전부 탐색 할 필요 없이, 정답이 될 가능성이 있는 방법만 찾는 것

예를 들어 찾을 단어 : cat

모든 후보들을 나열하지 않고

c 또는 a 또는 t 인 경우에만 조건을 찾아보는 것이다.


'''


'''

# 백트래킹을 정리 해보자면

solution이 될 가능성이 없는 candidate (후보) 는 더이상 탐색하지 않고
candidate를 포기 (backtrack) 하며 탐색하는 것

백트래킹을 사용하여 시간복잡도를 효율적으로 줄 일 수 있다.

하지만 모든 완전탐색 문제에서 백트래킹을 사용 할 수 없다.

예를 들어 첫 문제인 3개의 합을 구하는 문제인 경우 계산을 해보야지만 알 수 있다.

이런 경우는 백트래킹을 사용할 수 없다.

'''