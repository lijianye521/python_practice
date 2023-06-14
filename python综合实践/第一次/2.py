# 获取输入的数的个数
n = int(input())

# 获取输入的整数序列
numbers = list(map(int, input().split()))

# 初始化最大数为序列中的第一个数
max_number = numbers[0]

# 遍历整数序列，更新最大数
for number in numbers:
    if number > max_number:
        max_number = number

# 输出结果
print(max_number)

