def count_unvisited_cells(n, m, jumps):
    visited = [False] * n
    position = 0
    visited[position] = True
    for jump in jumps:
        position = (position + jump + 1) % n
        visited[position] = True
    return visited.count(False)


if __name__ == "__main__":
    n, m = map(int, input().split())
    jumps = list(map(int, input().split()))
    print(count_unvisited_cells(n, m, jumps))