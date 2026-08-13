class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results=[]
        maximum=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies >=maximum:
                results.append(True)
            else:
                results.append(False)
        return results
