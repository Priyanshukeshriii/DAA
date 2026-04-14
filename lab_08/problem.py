import random
import string

def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    
    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs_str.append(s1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    printDp(m,n,dp)

    return dp[m][n], "".join(reversed(lcs_str))

def printDp(m, n, dp):
    for i in range(m + 1):
        for j in range(n + 1):
            print(dp[i][j], end=" ")
        print()

def main():
    try:
        size1 = int(input("Enter size for the first sequence: "))
        size2 = int(input("Enter size for the second sequence: "))
        
        # Generating random uppercase strings
        seq1 = ''.join(random.choices(string.ascii_uppercase, k=size1))
        seq2 = ''.join(random.choices(string.ascii_uppercase, k=size2))
        
        print(f"\nSequence 1: {seq1}")
        print(f"Sequence 2: {seq2}")
        
        length, result = longest_common_subsequence(seq1, seq2)
        
        print(f"\nLength of LCS: {length}")
        print(f"LCS: {result if result else 'None'}")
        
    except ValueError:
        print("Please enter valid integers for sizes.")

if __name__ == "__main__":
    main()