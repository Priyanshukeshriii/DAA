def solve_n_queens():
    try:
        n = int(input("Enter the number of queens (N): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    
    board = [-1] * n
    results = []

    def is_safe(row, col):
        for i in range(row):
            
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def backtrack(row):
        if row == n:
            
            matrix = [["." for _ in range(n)] for _ in range(n)]
            for r in range(n):
                matrix[r][board[r]] = "Q"
            results.append([" ".join(r) for r in matrix])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
            

    backtrack(0)

   
    if not results:
        print(f"No solutions exist for N = {n}.")
    else:
        print(f"\nFound {len(results)} solutions for N = {n}:")
        for idx, sol in enumerate(results):
            print(f"\nSolution {idx + 1}:")
            for row in sol:
                print(row)
            print("-" * (n * 2))

if __name__ == "__main__":
    solve_n_queens()