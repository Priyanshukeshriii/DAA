import random

def solve_knapsack():
    
    try:
        n = int(input("Enter the number of items: "))
        capacity = int(input("Enter the capacity of the knapsack: "))
    except ValueError:
        print("Please enter valid integers.")
        return

    
    weights = [random.randint(1, 20) for _ in range(n)]
    profits = [random.randint(10, 100) for _ in range(n)]

    print("\n--- Generated Items ---")
    for i in range(n):
        print(f"Item {i+1}: Weight = {weights[i]}, Profit = {profits[i]}")

    
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                
                dp[i][w] = max(profits[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                
                dp[i][w] = dp[i-1][w]

    
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1) 
            w -= weights[i-1]

    
    print("\n--- Results ---")
    print(f"Maximum Profit: {dp[n][capacity]}")
    print(f"Total Items Selected: {len(selected_items)}")
    print("Selected Item Details:")
    for idx in selected_items:
        print(f" - Item {idx+1}: Weight {weights[idx]}, Profit {profits[idx]}")

if __name__ == "__main__":
    solve_knapsack()