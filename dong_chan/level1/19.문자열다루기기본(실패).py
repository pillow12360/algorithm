# 캐치 트라이
# def solution(s):
#     answer = True
    
#     try:
#         s = int(s)
#     except:
#         answer = False
        
#     if not len(str(s))==4 or len(str(s))==6:
#         answer = False 

#     return answer

def solution(s):
    
    try:
        int(s)
    except:
        return False


    return len(s)==4 or len(s)==6


s = "1234"

print(solution(s))