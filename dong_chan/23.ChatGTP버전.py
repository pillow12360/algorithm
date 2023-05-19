def solution(s):
    words = s.split()  # 단어를 공백을 기준으로 분할하여 리스트로 저장
    answer = []  # 변환된 단어들을 저장할 리스트

    for word in words:
        converted_word = ''
        for i in range(len(word)):
            if i % 2 == 0:
                converted_word += word[i].upper()
            else:
                converted_word += word[i].lower()
        answer.append(converted_word)

    return ' '.join(answer)  # 변환된 단어들을 공백을 기준으로 결합하여 반환

# 문제를 분석하고 답안이 정확히 작동하지 않는 케이스를 파악하기 위해 해당 문제의 내용과 주어진 코드를 살펴보겠습니다. "이상한 문자 만들기" 문제는 문자열에서 단어를 구분하는 공백을 기준으로 각 단어의 인덱스가 짝수인 경우 대문자로, 홀수인 경우 소문자로 변환하는 문제입니다.

#하지만 주어진 코드는 문제의 요구사항과 약간의 차이가 있습니다. 주어진 코드는 단어를 공백을 기준으로 분할한 후 각 단어의 문자 인덱스를 순회하면서 짝수 인덱스에 대문자로 변환하고, 홀수 인덱스에 소문자로 변환합니다. 그리고 모든 단어들을 하나의 문자열로 결합한 뒤 반환합니다.

#이 문제의 핵심은 각 단어에서 문자 인덱스를 순회하며 변환하는 것이 아니라, 단어의 인덱스가 짝수인 경우 대문자로, 홀수인 경우 소문자로 변환하는 것입니다.

#따라서 주어진 코드를 수정하여 문제의 요구사항에 맞게 작동하도록 변경해야 합니다. 아래는 수정된 코드입니다:


def solution(s):
    words = s.split()  # 단어를 공백을 기준으로 분할하여 리스트로 저장
    answer = []  # 변환된 단어들을 저장할 리스트

    for word in words:
        converted_word = ''
        for i in range(len(word)):
            if i % 2 == 0:
                converted_word += word[i].upper()
            else:
                converted_word += word[i].lower()
        answer.append(converted_word)

    return ' '.join(answer)  # 변환된 단어들을 공백을 기준으로 결합하여 반환



#위에 두 코드는 정답이 아님


# 정답 코드 
def solution(s):
    words = ' '.join(s.split()) # 공백 여러개인 경우 공백 하나로 변환
    words = s.split(" ")  # 단어를 공백을 기준으로 분할하여 리스트로 저장

    answer = []  # 변환된 단어들을 저장할 리스트

    for word in words:
        converted_word = ''
        for i in range(len(word)):
            if i % 2 == 0:
                converted_word += word[i].upper()
            else:
                converted_word += word[i].lower()
        answer.append(converted_word)

    return ' '.join(answer)  # 변환된 단어들을 공백을 기준으로 결합하여 반환