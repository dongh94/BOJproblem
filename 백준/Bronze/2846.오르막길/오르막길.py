import sys

n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))

f_h = l[0]
m_h = 0
result = []
for i in l:
    if i > f_h:
        m_h += (i-f_h)
        f_h = i
    else:
        result.append(m_h)
        f_h = i
        m_h = 0
result.append(m_h)
print(max(result))