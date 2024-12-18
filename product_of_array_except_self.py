from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

if __name__=='__main__':
    print(":arrays and hashing:")
    nums = [1,2,3,4] 

    s1 = Solution()
    print(s1.productExceptSelf(nums))  