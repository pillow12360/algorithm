def solution(s):
    answer = ''
    index = 0 
    if len(s) % 2 != 0:
      index = int((len(s)-1)/2)
      s = s[index]
    else:
      index = int((len(s))/2-1)
      s = s[index]+s[index+1]
    answer = s
    return answer




s = "abcdwqxs"	

print(solution(s))