# 10월 29일 화

n, m = map(int,input().split())
num_list = []

def backtrack(m, num_list):
    if len(num_list) == m:
        print(" ".join(map(str, num_list)))
        return

    for i in range(1, n+1):
        if not num_list or i >= num_list[-1]:
            num_list.append(i)
            backtrack(m, num_list)
            num_list.pop()

backtrack(m, num_list)