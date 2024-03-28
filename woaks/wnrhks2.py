nums1 = [10, 9, 2, 5, 3, 7, 101, 18]


def length_of_lis(nums):
    lengths = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                lengths[i] = max(lengths[i], lengths[j] + 1)

    max_length = max(lengths)

    return max_length

print(length_of_lis(nums1))


