def solve(m, n):
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    return dp[m - 1][n - 1]

def main():
    m, n = map(int, input().split())
    print(solve(m, n))

if __name__ == "__main__":
    main()
