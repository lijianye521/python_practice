def solveNQueens(n):
    def can_place(row, col):
        for i in range(row):
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                return False
        return True

    def place_queen(row, n):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if can_place(row, col):
                board[row] = col
                place_queen(row + 1, n)

    result = []
    board = [-1] * n
    place_queen(0, n)
    return len(result)

def main():
    n = int(input())
    print(solveNQueens(n))

if __name__ == "__main__":
    main()
