def two_sum(nums, target):
    num_map={}

    for index, number in enumerate(nums):
        complement = target - number

        if complement in num_map:
            return [num_map[complement], index]
        num_map[number] = index
    return []
print(two_sum([2,4,6,7], 13))