def LongestIncreasingSequence(arr):
    lis = []
    for (index, value) in enumerate(arr):
        lc = [lis[sub_index] for (sub_index, sub_value) in enumerate(arr[:index]) if sub_value < value] or [[]]
        lc_max = max(lc, key=len)
        lis.append(lc_max + [value])
        print(lis)
    return max(lis, key=len)


print(LongestIncreasingSequence([10, 12, 4, 6, 100, 2, 56, 34, 79]))
