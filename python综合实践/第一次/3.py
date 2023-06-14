def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b


# 获取输入的n
n = int(input())

# 调用fibonacci函数计算第n个数
result = fibonacci(n)

# 输出结果
print(result)