class Solution:
    def climbStairs(self, n:int) -> int:
            one, two = 1,1
            for i in range(n-1):
                  temp = one
                  one = one + two
                  two = temp
            return one      
                  

if __name__ == '__main__':

    s1 = Solution()
    print(s1.climbStairs(5))
    print(s1.climbStairs(6))

    #1,1,2,3,5,8