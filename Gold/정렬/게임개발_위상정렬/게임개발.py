import sys
sys.stdin = open("게임게발.txt")

# 1. 중요한 건 선수객체가 필요하다는 것.
from collections import defaultdict, deque

N = int(input())  # 건물 개수
ans = [0] * (N + 1)  # 최종 정답 리스트(각 건물 짓는 총 필요 시간)
cost = [0] * (N + 1)  # 각 건물 짓는 순수시간
degree = [0] * (N + 1)  # 진입차수 리스트
Q = deque()

graph = list([] for _ in range(N+1)) # 간선표현

for i in range(1, N + 1):
    temp = list(map(int, input().split()))  # 10, 1, -1
    cost[i] = temp[0]

    for ele in temp[1:-1]:
        graph[ele].append(i)  # ele -> i로가는 방향(i지을 때, ele 필요하다)
        degree[i] += 1  # i의 진입차수 +1

# 초기에 진입차수가 0인 건물들 넣어주기
for i in range(1, N + 1):  # 진입차수가 0인 노드를 Q에 넣어주기, ans에 비용 업데이트
    if degree[i] == 0:
        Q.append(i)
        ans[i] = cost[i]

while Q:  # Q에 있는 노드들의 간선을 제거하면서, ans값 업데이트
    now = Q.popleft()
    for e in graph[now]:
        degree[e] -= 1
        # 한 건물이 여러건물을 지어야 지을 수 있는 경우, 제일 오래걸리는 건물 짓고, 지을 수 있도록 max로 갱신
        ans[e] = max(ans[e], cost[e] + ans[now])
        if degree[e] == 0:  # 진입차수가 0이 되었으면 Q에 넣어주기
            Q.append(e)

print(*ans[1:], sep='\n')