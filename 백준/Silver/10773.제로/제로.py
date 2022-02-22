N = int(input())
stack = []
top = -1
for n in range(N):
    M = int(input())
    if M:
        stack.append(M)
    else:
        stack.pop()
print(sum(stack))