import sys
n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))
m = 100/max(l)
result = []
for i in l:
    result.append(i*m)
    
print(sum(result)/n)