#!/usr/bin/env python3

def longestArithSeqLength(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)

    if n <= 2:
        return n

    longest_length = 1
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            diff = nums[j] - nums[i]
            current_length = 2
            k = j + 1

            while k < n and nums[k] == nums[j] + diff:
                current_length += 1
                j = k
                k += 1
            longest_length = max(longest_length, current_length)
    return longest_length

