import sys

a = int(sys.stdin.readline())
order_list = list(map(int,sys.stdin.readline().strip().split()))
bin = []

for i in range(a):
    if order_list[i] == 0:
        bin.insert(i,i+1)
    elif order_list[i] > 0:
        bin.insert(i-order_list[i], i+1)

for i in bin:
    print(i, end=' ')