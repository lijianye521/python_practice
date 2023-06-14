
def dfs(s, n):
    if len(s) == n:
        print(s)
    else:
        for c in range(ord('a'), ord('a')+n):
            dfs(s+chr(c), n)

def main():
    n = int(input().strip())
    dfs('', n)

if __name__ == "__main__":
    main()
