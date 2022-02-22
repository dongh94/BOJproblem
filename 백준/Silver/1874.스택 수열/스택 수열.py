n = int(input())

stack = []
cnt = 0
flag = True
result = []
for i in range(n):
    m = int(input())

    while cnt < m:
        cnt += 1
        stack.append(cnt)
        result.append('+')

    if stack[-1] == m:
        stack.pop()
        result.append('-')
    else:
        flag = False
        break

if flag == False:
    print('NO')
else:
    for i in result:
        print(i)