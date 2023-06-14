# 获取输入的左边界和右边界
M, N = map(int, input().split())

# 初始化和为0
sum = 0

# 遍历区间内的自然数，包括左右边界
for num in range(M, N + 1):
    sum += num

# 输出结果
print(sum)

