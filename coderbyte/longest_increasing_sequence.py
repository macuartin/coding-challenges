# challenge: https://coderbyte.com/information/Longest%20Increasing%20Sequence

def LongestIncreasingSequence(arr):
    lis = []
    for (index, value) in enumerate(arr):
        lc = [lis[sub_index] for (sub_index, sub_value) in enumerate(arr[:index]) if sub_value < value] or [[]]
        lc_max = max(lc, key=len)
        lis.append(lc_max + [value])
    return len(max(lis, key=len))

# keep this function call here 
print LongestIncreasingSequence(raw_input())
