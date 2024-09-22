

from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1 # ord gets the asscii value
            ans[tuple(count)].append(s)
        return ans.values()

if __name__ == '__main__':
    lst_strings = ["ant","tan","cat","tac"]
    print(groupAnagrams(lst_strings)) 