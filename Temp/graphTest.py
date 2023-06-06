# g = [0, 8, 6, 7, 4, 1, 3, 2, 5]
# p = [1, 2, 3, 4, 5, 6, 7, 8]
# import sys
# sys.setrecursionlimit(1000)
# def f(i):
#     if i != g[i]:
#         g[i] = f(g[i])
#     return g[i]
#
# f(1)
#
# print(p)
#
#
# p = [i for i in range(V+1)]
#
# def find_set(x):
#     if x != p[x]:
#         p[x] = find_set(p[x])
#     return p[x]

# p = [i for i in range(8)]
p = [0, 8, 6, 7, 4, 1, 3, 2, 5]
# ===================================================
p[2] = 1; p[3] = 2; p[4] = 3;
print(p)

def find_set1(x):
    while x != p[x]: # 대표 정점이 아니면,
        x = p[x]
    return x

def find_set2(x):
    if x == p[x]:
        return p[x]
    else:
        p[x] = find_set2(p[x])
        return p[x]

def find_set3(x):
    if x!= p[x]:
        p[x] = find_set3(p[x])
    return p[x]

print(find_set3(4))
print(p)
