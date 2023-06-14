def find_smaller_dividend(dividend, divisor):
    if dividend % (divisor + 1) == 0:
        return dividend // (divisor + 1)
    else:
        return 'No solution'


if __name__ == "__main__":
    dividend, divisor = map(int, input().split())
    print(find_smaller_dividend(dividend, divisor))