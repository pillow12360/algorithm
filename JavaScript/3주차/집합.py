import sys

def solve():
    S = set()
    all_set = set(range(1, 21))  # {1, 2, ..., 20}
    output = sys.stdout.write  # 출력 최적화

    M = int(sys.stdin.readline().strip())  # 첫 번째 줄에서 M 받기

    for _ in range(M):
        command = sys.stdin.readline().strip()
        
        if command.startswith("add"):
            S.add(int(command[4:]))  # "add X"에서 X 추출 (빠른 문자열 슬라이싱)
        elif command.startswith("remove"):
            S.discard(int(command[7:]))  # "remove X"에서 X 추출
        elif command.startswith("check"):
            output("1\n" if int(command[6:]) in S else "0\n")  # 바로 출력
        elif command.startswith("toggle"):
            x = int(command[7:])
            if x in S:
                S.remove(x)
            else:
                S.add(x)
        elif command == "all":
            S = set(range(1, 21))  # all_set 사용 안하고 새로운 set 생성
        elif command == "empty":
            S.clear()  # 기존 set을 비움 (새로운 객체 생성 X)

solve()
