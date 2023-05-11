from collections import deque
import sys
sys.stdin=open("크게만들기.txt")

N, K = map(int, input().split())
input_str = input().strip()

d = deque()

for i in range(N):
    while d and K and d[-1] < input_str[i]:
        d.pop()
        K -= 1
    d.append(input_str[i])

for i in range(len(d) - K):
    print(d[i], end="")

