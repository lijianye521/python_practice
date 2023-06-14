def min_packages():
    while True:
        # products[5] ~ products[0] -> size of 6*6 ~ 1*1 boxes
        # Read input
        products = list(map(int, input().split()))

        # If input is all zeros, break
        if sum(products) == 0:
            break

        # Initialize the number of packages
        packages = products[5]

        # Handle 5*5 boxes
        packages += products[4]
        products[0] -= min(products[4]*11, products[0])

        # Handle 4*4 boxes
        packages += products[3]
        if products[3]*5 <= products[1]:
            products[1] -= products[3]*5
        else:
            products[0] -= min((products[3]*5 - products[1])*4, products[0])
            products[1] = 0

        # Handle 3*3 boxes
        packages += (products[2] + 3) // 4
        rem = [0, 5, 3, 1, 0]
        if rem[products[2] % 4] <= products[1]:
            products[1] -= rem[products[2] % 4]
            products[0] -= min((4 - products[2] % 4) * 4, products[0])
        else:
            products[0] -= min((36 - products[2] % 4 * 9 - products[1] * 4), products[0])

        # Handle 2*2 boxes
        packages += (products[1] + 8) // 9
        if products[1] % 9 != 0:
            products[0] -= min((9 - products[1] % 9) * 4, products[0])

        # Handle 1*1 boxes
        packages += (products[0] + 35) // 36

        print(packages)


# Testing
min_packages()
