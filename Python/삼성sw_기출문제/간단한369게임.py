T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())

    for i in range(1,n+1):
            backsoo = ""

            for j in str(i):
                if j == '3' or j == '6' or j == '9':
                    backsoo += "-"
            if backsoo == "":
                print(i,end=" ")
            elif backsoo == "-":
                print(backsoo, end=" ")
            else:
                print(backsoo, end="")