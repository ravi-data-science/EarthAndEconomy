
from typing import List
import math
import os
import random
import re
import sys
from typing import Counter

def hasDuplicate(nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

def is_anagram_using_sorted(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

def is_anagram_using_maps(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map, t_map = {}, {}

        for i in range(len(s)):
            s_map[s[i]] = 1 + s_map.get(s[i], 0)
            t_map[t[i]] = 1 + t_map.get(t[i], 0)
        return s_map == t_map

def using_counter_creating_hashmap(s: str, t: str):
    return Counter(s) == Counter(t)     

def twoSum(nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
            print(prevMap)

def getConcatenation(nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            result.append(num)  # Add each element from nums
        for num in nums:
            result.append(num)  # Add each element again
        return result

def getConcatenation1(nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * (2 * n)  # Create a new list of size 2n
        for i in range(n):
            result[i] = nums[i]      # Copy the first part
            result[i + n] = nums[i]  # Copy the second part
        return result

def getConcatenation2(nums: List[int]) -> List[int]:
        nums.extend(nums)  # Extend the list with itself
        return nums

def getConcatenation3(nums: List[int]) -> List[int]:
        return nums + nums  # Concatenate the list with itself

if __name__=='__main__':
    print("has dup::")
    nums = [1, 2, 3, 3]   
    hasDup = hasDuplicate(nums) 
    print(hasDup)

# are two strings anagrams
    print("\nis anagrams::")
    print(is_anagram_using_maps("tram","mart")) 

#two sum
    print("\ntwo sum")
    lst_ints = [5,7,6,10,5]
    print(twoSum(lst_ints, 10))     

    #concatenate lists
    print("\n concatenate lists::")
    print(getConcatenation(lst_ints)) 
    print(getConcatenation1(lst_ints)) 
    print(getConcatenation2(lst_ints)) 
    print(getConcatenation3(lst_ints)) 



