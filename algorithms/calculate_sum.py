def calc_sum(n):
    if n == 1:
        return 1
    else:
        return n + calc_sum(n - 1) # calc_sum() returns 5 and then 1    # 5 + 1 = 6


sum = calc_sum(3)
print(sum)  # Output: 6
