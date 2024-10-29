from collections import deque
from typing import List



def search(nums: List[int], target: int) -> int:
    print(nums)
    l, r = 0, len(nums) - 1

    for i in range(nums):
        print(i)

    while l <= r:
        m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1

if __name__ == '__main__':
     nums = [6,5,4,8,9,2,3]
     nums.sort()
     print(nums)

     print(search(nums,8))