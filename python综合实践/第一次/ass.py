def book_purchase_plans(n, amounts):
    books_price = [10, 20, 50, 100]
    plans = [0 for _ in range(1001)]
    plans[0] = 1
    for price in books_price:
        for i in range(price, 1001):
            plans[i] += plans[i-price]
    for i in range(n):
        print(plans[amounts[i]])

def main():
    n = int(input().strip())
    amounts = []
    for _ in range(n):
        amounts.append(int(input().strip()))
    book_purchase_plans(n, amounts)

if __name__ == "__main__":
    main()
