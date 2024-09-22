
#!/bin/python3

import math
import os
import random
import re
import sys
from typing import Counter

def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map, t_map = {}, {}

        for i in range(len(s)):
            s_map[s[i]] = 1 + s_map.get(s[i], 0)
            t_map[t[i]] = 1 + t_map.get(t[i], 0)
        return s_map == t_map

def using_counter_creating_hashmap(s: str, t: str):
    return Counter(s) == Counter(t)

def using_sorted_creating_hashmap(s: str, t: str):
    return sorted(s) == sorted(t)

if __name__ == '__main__':
     
    print(isAnagram("tram","mart")) 
    print(using_counter_creating_hashmap("tram","mart"))
    print(using_sorted_creating_hashmap("tram","mart"))

#or just sort it 