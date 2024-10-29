def lengthOfLastWord(s: str) -> int:
        """
	one shortcut
	"""
	#	return len(s.split()[-1])
        c = 0
        for i in s[::-1]:
            if i == " ":
                if c >= 1:
                    return c
            else:
                c += 1
        return c

def lengthOfLastWord_1(s: str) -> int:
     #start at last position
     i = len(s) -1 
     length = 0
     while s[i] == " ":
          i -= 1
     while i >= 0 and s[i] != " ":
          length += 1
          i -= 1
     return length



if __name__=='__main__':
    print("::")
    # nums = [4,5,7,8,6,3,2] 
    print(lengthOfLastWord_1(" this is a string "))