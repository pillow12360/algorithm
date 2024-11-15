
N = int(input())

command = input()

#위, 아래, 왼, 오
cur_row, cur_col = 1, 1
delta = [(-1, 0), (+1, 0), (0, -1), (0, 1)]


def move(i,cur_row,cur_col):
    global delta
    row, col = delta[i]
    next_row = cur_row + row
    next_col = cur_col + col

    if 1 <= next_row <= N and 1 <= next_col <= N:
        cur_row = next_row
        cur_col = next_col

    return cur_row, cur_col

for cur_com in command:

    if cur_com == "U":
        cur_row, cur_col = move(0,cur_row,cur_col)

    elif cur_com == "D":
        cur_row, cur_col = move(1,cur_row,cur_col)

    elif cur_com == "L":
        cur_row, cur_col = move(2,cur_row,cur_col)

    elif cur_com == "R":
        cur_row, cur_col = move(3,cur_row,cur_col)

print(cur_row,cur_col)