import sys
sys.stdin = open("NQueen.txt")
sys.setrecursionlimit(10000)

n = int(sys.stdin.readline())
queen_col = [0] * 15
cnt = 0

def promising(row):
    for i in range(row):
        # If there is a queen in the same column or on the diagonal, return false
        if (queen_col[row] == queen_col[i]) or (abs(row - i) == abs(queen_col[row] - queen_col[i])):
            return False
    return True

def dfs(row):
    global cnt
    # If we have found a case of placing n queens in n rows
    if row == n:
        cnt += 1  # Update count
        return  # Move to the next column (explore other cases)
    for col in range(n):
        queen_col[row] = col
        # If it is promising, move to the next row (depth first search)
        # Otherwise, move to the next column of the same row (pruning)
        if promising(row):
            dfs(row + 1)

# Main function

dfs(0)
print(cnt)
