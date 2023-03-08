import sys; sys.stdin=open("체스판다시칠하기.txt")

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

cnt = []
for r in range(N-7):
    for c in range(M-7):
        w_start = 0
        b_start = 0
        for i in range(r, r+8):
            for j in range(c, c+8):
                if (i+j) % 2 == 0: # 첫 값이 W라면
                    if arr[i][j] == "W":
                        b_start += 1 # B였을때를 +1
                    else:
                        w_start += 1
                else:
                    if arr[i][j] == "W":
                        w_start += 1
                    else:           # 다음 값이 B라면
                        b_start += 1 # B였을때를 +1
        cnt.append(min(w_start, b_start))
print(min(cnt))