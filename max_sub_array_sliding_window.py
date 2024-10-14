from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]

        total = 0
        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
        return res
    
if __name__ == '__main__':
    nums = [6,5,-1,4,8,-30,-3,9,2,3]
    print(nums)

    sol = Solution()
    print(sol.maxSubArray(nums))