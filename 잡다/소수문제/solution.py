def solution(A, B, C):
    # 첫 번째 연산과 두 번째 연산 처리
    result = []

    # 첫 번째 분수 쌍 처리 (인덱스 0,1)
    first_op = C[0]
    if first_op in ['+', '-', '*', '/']:
        first_result = calculate_arithmetic(A[0:2], B[0:2], first_op)
    else:  # =, <, >
        first_result = compare_fractions(A[0:2], B[0:2], first_op)
    result.append(first_result)

    # 두 번째 분수 쌍 처리 (인덱스 2,3)
    second_op = C[1]
    if second_op in ['+', '-', '*', '/']:
        second_result = calculate_arithmetic(A[2:4], B[2:4], second_op)
    else:  # =, <, >
        second_result = compare_fractions(A[2:4], B[2:4], second_op)
    result.append(second_result)

    return result


def calculate_arithmetic(A, B, operator):
    if operator == '+':
        numerator = A[0] * B[1] + B[0] * A[1]
        denominator = A[1] * B[1]
    elif operator == '-':
        numerator = A[0] * B[1] - B[0] * A[1]
        denominator = A[1] * B[1]
    elif operator == '*':
        numerator = A[0] * B[0]
        denominator = A[1] * B[1]
    else:  # operator == '/'
        numerator = A[0] * B[1]
        denominator = A[1] * B[0]

    # 약분
    gcd_val = gcd(abs(numerator), abs(denominator))
    numerator = numerator // gcd_val
    denominator = denominator // gcd_val

    # 부호 처리
    if denominator < 0:
        numerator = -numerator
        denominator = -denominator

    return numerator


def compare_fractions(A, B, operator):
    # 통분하여 비교
    numerator1 = A[0] * B[1]
    numerator2 = B[0] * A[1]

    if operator == '=':
        return 1 if numerator1 == numerator2 else 0
    elif operator == '<':
        return 1 if numerator1 * A[1] * B[1] < numerator2 * A[1] * B[1] else 0
    else:  # operator == '>'
        return 1 if numerator1 * A[1] * B[1] > numerator2 * A[1] * B[1] else 0


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def test_solution():
    # 예제에서 제공된 테스트 케이스들
    test_cases = [
        {
            'A': [1, 1, 1, 2],
            'B': [2, 3, 12, 1],
            'C': "=*",  # C[0]='=', C[1]='*'
            'expected': [1, 1]  # 예상 결과
        },
        {
            'A': [1, 1, 1, 1],
            'B': [2, 3, 4, 3],
            'C': "+<",  # C[0]='+', C[1]='<'
            'expected': [0, 1]  # 예상 결과
        }
    ]

    # 추가 테스트 케이스들
    additional_tests = [
        {
            'A': [1, 2, 3, 4],
            'B': [2, 3, 5, 6],
            'C': "+>",
            'expected': [1, 1]
        },
        {
            'A': [1, 3, 2, 5],
            'B': [1, 6, 1, 5],
            'C': "*=",
            'expected': [1, 0]
        },
        {
            'A': [2, 3, 4, 5],
            'B': [3, 4, 5, 6],
            'C': "/<",
            'expected': [1, 1]
        }
    ]

    # 모든 테스트 케이스 실행
    all_tests = test_cases + additional_tests
    for i, test in enumerate(all_tests, 1):
        result = solution(test['A'], test['B'], test['C'])
        success = result == test['expected']
        print(f"Test {i}:")
        print(f"Input: A={test['A']}, B={test['B']}, C={test['C']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")
        print(f"Result: {'Pass' if success else 'Fail'}")
        print("-" * 50)


if __name__ == "__main__":
    test_solution()