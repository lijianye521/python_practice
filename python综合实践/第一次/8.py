def find_intervals(M):
    intervals = []
    for L in range(1, M):
        interval_sum = 0
        for R in range(L, M):
            interval_sum += R
            if interval_sum == M:
                intervals.append((L, R))
                break
            elif interval_sum > M:
                break
    return intervals


# 从输入中读取M的值
M = int(input())

# 计算满足条件的区间
intervals = find_intervals(M)

# 输出结果
for interval in intervals:
    print(f"[{interval[0]},{interval[1]}]")