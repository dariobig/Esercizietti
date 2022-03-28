# https://ttzztt.gitbooks.io/lc/content/continuous-subarray-sum.html
# Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be # strictly increasing.
# Input: nums = [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
# Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
# 4.

# %%
from typing import List

def find_subarray(nums: List[int]) -> int:
    num_set = set(nums)
    longest = 0

    for n in nums:
        # start of a sequence:
        if n -1 not in num_set:
            length = 0
            while n + length in num_set:
                length += 1
            longest = max(length, longest)
    return longest

# %%
nums = [1, 3, 5, 4, 100, 200]
print(find_subarray(nums))

