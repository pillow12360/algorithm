def solution(array, commands):
    answer = []
    temps = []

    answer2 = []
    for i in range(len(commands)):
        temps = commands[i]

        i = temps[0]
        j = temps[1]
        k = temps[2]

        answer2 = sorted(array[i-1:j])

        answer.append(answer2[int(k-1)])
            
    return answer

array = [1, 5, 2, 6, 3, 7, 4]	
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array,commands))
        