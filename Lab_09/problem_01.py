import random

def matrix_chain_order(p, n):
    dp = [[0] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]

    for length in range(2, n):  
        for i in range(1, n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i-1] * p[k] * p[j]

                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    return dp, split


def print_parenthesis(split, i, j):
    if i == j:
        return f"A{i}"
    return f"({print_parenthesis(split, i, split[i][j])} x {print_parenthesis(split, split[i][j] + 1, j)})"


n = int(input("Enter number of matrices: "))

p = [random.randint(5, 50) for _ in range(n + 1)]

print("\nGenerated matrix dimensions:")
for i in range(1, n + 1):
    print(f"A{i}: {p[i-1]} x {p[i]}")

dp, split = matrix_chain_order(p, n + 1)

print("\nMinimum number of multiplications:", dp[1][n])
print("Optimal Parenthesization:", print_parenthesis(split, 1, n))