

from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
        lst_group_anagrams = defaultdict(list)

        for s in strs:
            lst_alphabet_pos_num = [0] * 26
            for c in s:
                lst_alphabet_pos_num[ord(c) - ord("a")] += 1 # ord gets the asscii value
            lst_group_anagrams[tuple(lst_alphabet_pos_num)].append(s)
        return lst_group_anagrams.values()

if __name__ == '__main__':
    lst_strings = ["ant","tan","cat","tac"]
    print(groupAnagrams(lst_strings)) 