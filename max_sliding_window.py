# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# https://www.youtube.com/watch?v=DfljaUwZsOk&ab_channel=NeetCode

# Return the max sliding window.
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]

#%%
from typing import List, Deque
from collections import deque

def window_max(nums: List[int], k: int) -> int:
    max_n = nums[0]
    output: List[int] = []
    window: Deque[int] = deque()
    max_w = max_n
    l = 0
    r = 0

    while r < len(nums):
        n = nums[r]
        print(f'window: {window}, n: {n}, l: {l}, r: {r}')
        while window and nums[window[-1]] < n:
            window.pop()
            print(f'window: {window}, n: {n}')

        if l + r > 0:
            window.append(r)
            # window is past the leftmost element:
            print(f'window: {window}, n: {n}')
            window.popleft()

        if window and r + 1 >= k:
            # window is big enough
            max_w = window[0]
            output.append(max_w)
            print(f'window: {window}, n: {n}')
        r += 1

    return output

print(window_max([1,-1], 1))
# %%
