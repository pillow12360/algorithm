n = int(input())

def three(time):
    if time == 0:
        return int(3)
    else:
        return three(time-1) * 3

print(three(n-1))
    