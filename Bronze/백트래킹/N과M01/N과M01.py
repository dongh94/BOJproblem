import sys

# N, M = map(int, sys.stdin.readline().split())
N, M = 4, 2
order = [0] * M
visited = [0]*(N+1)
result = []
answer = []

def DFS(k):
    if k == M:
        answer.append(order[:])
        return

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            order[k] = i
            DFS(k + 1)
            visited[i] = 0
DFS(0)
print(result)
print(answer)
# import sys
#
# N, M = map(int, sys.stdin.readline().split())
# array = [0] * M
# visited = [False] * (N+1)
# result = []
#
# def NM(m):
#     if m == M:
#         result.append(' '.join(map(str, array)))
#     else:
#         for k in range(1, N+1):
#             if not visited[k]:
#                 visited[k] = True
#                 array[m] = k
#                 NM(m+1)
#                 visited[k] = False
#
# NM(0)
# print('\n'.join(result))