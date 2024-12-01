
from typing import List


def hasDuplicate(nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

def hasDuplicate_1(nums: List[int]) -> bool:
        elements_set = set()

        for index,val in enumerate(nums):
            if val in elements_set:
               return True
            else:
               elements_set.add(val)
        return False

if __name__=='__main__':
    nums = [1, 2, 3, 3]   

    hasDup = hasDuplicate(nums) 
    print(hasDup)
