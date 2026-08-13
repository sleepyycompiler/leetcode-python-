class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        e=0
        for x in nums:
            c=0
            while(x>0):
              x=x//10
              c=c+1
            if(c%2==0):
               e=e+1
        return e