def solution(x):
    answer = False

    x = str(x)

    hap = 0

    for i in x:
        hap += int(i)

    a = int(x)/hap
    if float.is_integer(a):
        answer = True


    return answer

x= 18

print(solution(x))