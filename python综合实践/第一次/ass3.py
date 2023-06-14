
def remove_k_digits(input_str):
    num, k = input_str.split()
    k = int(k)
    for i in range(0, k):
        has_cut=False
        for j in range(0, len(num)-1):
            if num[j] > num[j+1]:
                num = num[:j] + num[j+1:]
                has_cut = True
                break
        if not has_cut:
            num = num[:len(num)-1]
    return num.lstrip('0') or '0'
# 使用方法
m = map(str, input())
print(remove_k_digits(m))  # 输出: "1219"
