import sys

sys.stdin = open("IQTest.txt")
sys.setrecursionlimit(1000)
input = sys.stdin.readline

# N = int(input())
# arr = list(map(int, input().split()))
#
# def calc(a, b):
#     return arr[N-1] * a + b
#
# def findAB(n):
#     cnt = 0
#     res = 0
#     if n == 1:
#         return 'A'
#
#     if n == 2 and arr[0] == arr[1]:
#         return arr[0]
#
#     for a in range(-100, 100):
#         for b in range(-100, 100):
#             used = 0
#             for i in range(n-1):
#                 if cnt > n-1:
#                     return 'A'
#                 if -100 <= abs(arr[i] * a + b) <= 100 and arr[i+1] == arr[i] * a + b:
#                     used += 1
#                 if used == n-1:
#                     cnt += 1
#                     res = calc(a, b)
#
#     if cnt == 0:
#         return 'B'
#
#     else:
#         return res
#
# answer = findAB(N)
# print(answer)

N = int(input())
arr = list(map(int, input().split()))

def findAB():
    if N == 1 :
        return "A"

    if N == 2 :
        if arr[0] != arr[1]:
            return "A"
        return arr[0]

    a = 0
    b = 0
    if arr[1] == arr[0]:
        a = 1
        b = 0
    else:
        a = (arr[2] - arr[1]) // (arr[1] - arr[0])
        b = arr[1] - (arr[0] * a)

    if calc(a, b):
        return arr[N - 1] * a + b
    else:
        return "B"

def calc(a, b):
    for i in range(N - 1):
        if arr[i + 1] != arr[i] * a + b:
            return False
    return True

answer = findAB()
print(answer)