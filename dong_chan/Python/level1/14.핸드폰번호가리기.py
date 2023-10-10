def solution(phone_number):
    answer = ''
    phone_number = list(phone_number)
    for i in range(len(phone_number)-4):
        phone_number[i] = "*"
    map(str,phone_number)
    answer = ''.join(s for s in phone_number)
    return answer