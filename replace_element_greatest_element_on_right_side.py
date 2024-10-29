from typing import List
def replaceElements(arr: List[int]) -> List[int]:
    rightMax = -1
    for i in range(len(arr) -1, -1, -1):
        print("rightMax::")
        print(rightMax)
        print("current")
        print(arr[i])
        newMax = max(rightMax, arr[i])
        print("newMax::")
        print(newMax)
        arr[i] = rightMax
        rightMax = newMax
    return arr

if __name__=='__main__':
    print("::")

    nums = [4,5,7,8,6,3,2] 
    print(replaceElements(nums))