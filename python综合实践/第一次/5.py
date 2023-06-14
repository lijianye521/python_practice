n = int(input())  # 输入n的值

# 初始化和为0
total_sum = 0

# 遍历从1到n的每个数字
for num in range(1, n + 1):
    # 将数字转换为字符串，用于判断是否包含2、0、1、9
    num_str = str(num)

    # 判断数字是否包含2、0、1、9
    if '2' in num_str or '0' in num_str or '1' in num_str or '9' in num_str:
        total_sum += num

# 输出满足条件的数字的和
print(total_sum)