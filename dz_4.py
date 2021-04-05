src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# src_gen = (el for el in src)
# print(next(src_gen))

result = []
for i in range(0, len(src)):
    if i + 1 == len(src):
        break
    elif src[i] < src[i+1]:
        result.append(src[i+1])

print(result)

# # result2 = []
# # for i in range(1,len(src)):
# #     if next(src_gen) < src[i]:
# #         print(src[i])
#
# result3 = [src[i] for i in range(1, len(src)) if next(src_gen) < src[i]]
# print(result3)
