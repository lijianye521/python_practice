def knapsack(n, m, w, v):
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if j < w[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1])
    return dp[n][m]

def main():
    n, m = map(int, input().strip().split())
    w = list(map(int, input().strip().split()))
    v = list(map(int, input().strip().split()))
    print(knapsack(n, m, w, v))

if __name__ == "__main__":
    main()
