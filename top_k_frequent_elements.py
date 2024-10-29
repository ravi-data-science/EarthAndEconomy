from typing import List
def topKFrequent(nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        print("map::")
        print(count)    
        for n, c in count.items():
            freq[c].append(n)

        print("freq:::") 
        print(freq)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            res += freq[i]
            if len(res) == k:
                return res
                

        # O(n)

"""
def topKFrequent_1(nums: List[int], k: int) -> List[int]:
        count = {}
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        print("map::")
        print(count)    

        val_list = list(count.values())

        val_list.sort()
        print(val_list)
  

        for index, val in val_list.items():
             print(val)
"""

if __name__=='__main__':
    print("::")
    nums = [4,5,7,8,6,3,2,4,7,8,8] 
    print(topKFrequent(nums,3))        