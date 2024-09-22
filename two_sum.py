
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

if __name__ == '__main__':
    lst_ints = [5,7,6,10,5]
    print(twoSum(lst_ints, 10))            