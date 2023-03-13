num = input()
temp_lst = [0]*10
for i in num:
    temp_lst[int(i)] += 1
for j in range(len(temp_lst)-1, -1, -1):
    for _ in range(temp_lst[j]):
        print(int(j), end='')