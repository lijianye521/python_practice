def cut_rectangles(m, n):
    count = 0
    while m != n:
        # 判断哪个边长更大，将其减去较小的边长得到新的边长
        if m > n:
            m -= n
        else:
            n -= m
        count += 1

    # 最后剩下的正方形也算作一个
    count += 1
    return count


# 读取输入的矩形边长
m, n = map(int, input().split())

# 调用函数计算能切割出的正方形数量
result = cut_rectangles(m, n)

# 输出结果
print(result)
