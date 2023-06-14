def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0, 1, 2] + [0]*(n-2)
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def main():
    n = int(input().strip())
    print(climb_stairs(n))

if __name__ == "__main__":
    main()
