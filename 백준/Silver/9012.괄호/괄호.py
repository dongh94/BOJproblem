def check_func(s):
    check = []
    top = -1
    for i in s:
        if i == '(' :
            check.append(i)
            top += 1
        elif i == ')':
            if top == -1:
                return 'NO'
            elif i == ')':
                if check[top] == '(':
                    check.pop()
                    top -= 1
                else:
                    return 'NO'

    if check:
        return 'NO'
    else:
        return 'YES'

t = int(input())
for tc in range(t):
    s = input()
    result = check_func(s)
    print(result)