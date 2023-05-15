import sys
sys.stdin = open("지뢰찾기.txt")
# 모든 지뢰의 수를 한 줄에 하나씩 출력
T = int(input())
for _ in range(T):
    result = 0
    N = int(input())
    S = input()
    mine = input()

    for i in range(N):
        if i == 0:
            if S[0] != '0' and S[1] != '0':
                S = S[:i] + chr(ord(S[i]) - 1) + S[i+1:]
                S = S[:i+1] + chr(ord(S[i+1]) - 1) + S[i+2:]
                result += 1
        elif i == N - 1:
            if S[N - 1] != '0' and S[N - 2] != '0':
                S = S[:i] + chr(ord(S[i]) - 1) + S[i+1:]
                S = S[:i-1] + chr(ord(S[i-1]) - 1) + S[i:]
                result += 1
        else:
            if S[i - 1] != '0' and S[i] != '0' and S[i + 1] != '0':
                S = S[:i-1] + chr(ord(S[i-1]) - 1) + S[i:i+1] + chr(ord(S[i]) - 1) + S[i+1:]
                S = S[:i+1] + chr(ord(S[i+1]) - 1) + S[i+2:]
                result += 1
    print(S)
    print(result)






