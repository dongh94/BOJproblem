import sys

a,b = [int(x)for x in sys.stdin.readline().split()]
ls = [int(x)for x in sys.stdin.readline().split()]
max_ondo = sum(ls[:b])
result = [max_ondo]
for i in range(a-b):
    max_ondo = max_ondo - ls[i] + ls[i+b]
    result.append(max_ondo)
print(max(result))