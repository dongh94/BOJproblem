import sys
sys.stdin = open("한수.txt")
N = int(input())
def hansu(N):
    start = 0
    if N < 100:
        return N
    if N >= 100:
        start += 99
        for i in range(100, N+1):
            place = list(map(int, str(i)))
            if place[0] - place[1] == place[1] - place[2]:
                start += 1
    return start
answer = hansu(N)
print(answer)

