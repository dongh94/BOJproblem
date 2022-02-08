import sys

f = 1
for i in range(3):
    n = int(sys.stdin.readline())
    f *= n 
    
f = str(f)
for i in range(10):
    result=0
    for s in f:
        if str(i) == s:
            result += 1
    print(result)