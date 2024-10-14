# 10월 14일 월


from collections import deque

N = int(input())

if N == 1 or N == 2:
    print(N)
else:
    str = deque()

    for i in range(1,N+1):
        str.append(i)

    # print(str)

    while len(str) > 0:

        str.popleft()
        # print(str)

        tem = str.popleft()
        str.append(tem)

        # print(str)

        if len(str) == 2:
            print(str.pop())
            break





'''

n = 4

1 2 3 4

2 3 4

3 4 2

1번

4 2

2 4

4

2번

답 : 4

'''


'''
1 2 3 4 5 6

2 3 4 5 6

3 4 5 6 2




'''

def last_card_remaining_math(N):
    # Find the largest power of 2 less than or equal to N
    power_of_two = 1
    while power_of_two * 2 <= N:
        power_of_two *= 2

    # Calculate the last remaining card
    remaining_card = 2 * (N - power_of_two)
    return remaining_card

# Example usage
N = 4
print("The last remaining card is:", last_card_remaining_math(N))