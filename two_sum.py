
#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List



def twoSum(nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
            print(prevMap)
def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        map_elements = {}
        for index, val in enumerate(nums):
            diff = target - val
            if diff in map_elements:
                return [map_elements[diff],index]
            map_elements[val] = index
           

if __name__ == '__main__':
    lst_ints = [5,7,6,10,5]
    print(twoSum(lst_ints, 10))            