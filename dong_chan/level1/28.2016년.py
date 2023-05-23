# 파이썬 datetiem패키지

import datetime as date

def solution(a, b):
    answer = ''

    x = date.date(2016,a,b)
    week = x.weekday()

    if week == 6:
        week = "SUN"
    elif week == 0:
        week = "MON"
    elif week == 1:
        week = "TUE"
    elif week == 2:
        week = "WED"
    elif week == 3:
        week = "THU"
    elif week == 4:
        week = "FRI"
    elif week == 5:
        week = "SAT"

    answer = week
    return answer


a = 5
b = 24

print(solution(a,b))