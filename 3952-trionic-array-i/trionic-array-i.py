class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n=len(nums)
        if nums[0]>=nums[1] or n<4: return False
        q, t, i=0, 0, 2
        while i<n:
            while i<n and nums[i-1]<nums[i]: i+=1
            if i<n and nums[i-1]==nums[i]: return False

            while i<n and nums[i-1]>nums[i]: i+=1
            if i<n and nums[i-1]==nums[i]: return False

            q=i
            if not(1<q<n): return False
            while i<n and nums[i-1]<nums[i]: i+=1
            t=i
            if t<n: return False
            i+=1
        return True