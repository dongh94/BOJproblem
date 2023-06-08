arr = [[1,2,3,4] for _ in range(3)]
print(arr.count(arr[1]))

arr = [[1, 2, 3, 4] for _ in range(3)]
count = sum(row == arr[1] for row in arr)
print(count)

print( sum(sum(row) for row in arr))
