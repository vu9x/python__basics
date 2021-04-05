n = 15
nums_gen = (num_odd for num_odd in range(1, n + 1) if num_odd % 2 != 0)

for i in nums_gen:
    print(i)
