import sys
result = 0
idx = 0
for i in range(5):
    a = map(int, sys.stdin.readline().split())
    s = sum(a)
    if s > result:
        result = s
        idx = i+1
        
print(idx, result)