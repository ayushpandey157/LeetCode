class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        occDict = dict(Counter(nums))

        for key in occDict:
            
            if occDict[key] == len(nums)/2:
                return key