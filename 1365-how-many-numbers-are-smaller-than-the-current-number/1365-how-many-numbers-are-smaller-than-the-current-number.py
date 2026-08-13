class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        results=[]
        for i in range(len(nums)):
            c=0
            j=0
            while(j<len(nums)):
                if(j!=i):
                 if(nums[j]<nums[i]):
                    c=c+1
                j=j+1
            results.append(c)     
        return(results)