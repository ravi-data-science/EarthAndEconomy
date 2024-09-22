
from typing import List


def is_palindrome(str_1: str) -> bool:
        clean_str = ""

        for c in str_1:

            if c.isalnum():
                clean_str += c.lower()
        print(clean_str)       
         
        #Create a slice that starts at the end of the string, and moves backwards.

#In this particular example, the slice statement [::-1] means start at the end of the string 
#and end at position 0, move with the step -1, negative one, which means one step backwards. 
        return clean_str == clean_str[::-1]

def ispalindrome_with_pointers(s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not alphaNum(s[l]):
                l += 1
            while r > l and not alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
    
def alphaNum(c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))

if __name__=='__main__':
    str_1 = "malayalam  ;"  

    is_palin = is_palindrome(str_1) 
    print(is_palin)

    print(ispalindrome_with_pointers(str_1))